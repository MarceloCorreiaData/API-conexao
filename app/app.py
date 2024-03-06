from flask import Flask
from flasgger import Swagger
from config import Config
from app.models.model_preprocessing import preprocess_data
from app.models.model_training import train_and_save
import numpy as np
import pickle

app = Flask(__name__)
app.config.from_object(Config)

# Importação do blueprint
from app.routes.arquivo_de_rotas import mod
app.register_blueprint(mod)

# Configuração do Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from the blueprint!'})

@app.route('/train', methods=['POST'])
def train_model_endpoint():
    """
    Endpoint para treinar um modelo
    ---
    parameters:
      - name: data
        in: body
        required: true
        schema:
          id: DataInput
          type: object
          properties:
            data:
              type: object
              properties:
                features:
                  type: array
                  items:
                    type: array
                    items:
                      type: number
                  example: [[0.5, 1.3, 3.3], [1.1, 2.2, 3.3], [0.7, 1.5, 2.8]]
                labels:
                  type: array
                  items:
                    type: number
                  example: [0, 1, 0]
    responses:
      200:
        description: Modelo treinado com sucesso
      400:
        description: Entrada inválida
    """
    data = request.get_json()
    
    if not data or not 'data' in data:
        return jsonify({'error': 'Entrada inválida'}), 400

    data_content = data.get('data')
    
    if not data_content or not 'features' in data_content or not 'labels' in data_content:
        return jsonify({'error': 'Campos features e labels são necessários'}), 400

    data_content = preprocess_data(data_content)

    try:
        features = np.array(data_content.get('features'))
        labels = np.array(data_content.get('labels'))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    if len(features) == 0 or len(features) != len(labels):
        return jsonify({'error': 'Dados de entrada inválidos'}), 400
    
    model = train_and_save(features, labels)
    return jsonify({'success': 'Modelo treinado e salvo com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)

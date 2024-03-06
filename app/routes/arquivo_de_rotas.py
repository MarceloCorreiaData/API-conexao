from flask import Blueprint, jsonify

# Cria um blueprint chamado 'mod'
mod = Blueprint('mod', __name__)

# Uma rota de exemplo associada a este blueprint
@mod.route('/')
def index():
    return jsonify({"message": "Hello from the blueprint!"})

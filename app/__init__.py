from flask import Flask
from config import Config
from app.app import app

app = Flask(__name__)
app.config.from_object(Config)

# Importação do blueprint
from app.routes.arquivo_de_rotas import mod
app.register_blueprint(mod)

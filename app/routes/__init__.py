# /app/routes/__init__.py

from flask import Blueprint

# Definindo o blueprint
mod = Blueprint('mod', __name__)

# Importando as rotas após definir o blueprint para evitar importações circulares
from . import arquivo_de_rotas

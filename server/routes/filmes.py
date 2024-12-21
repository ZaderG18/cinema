from flask import Blueprint, jsonify
from models import Filme  # Agora importa apenas o modelo Filme

filmes_bp = Blueprint('filmes', __name__)

@filmes_bp.route('/filmes', methods=['GET'])
def get_filmes():
    # Consultando todos os filmes no banco de dados
    filmes = Filme.query.all()
    
    # Convertendo os objetos Filme para dicionários
    filmes_list = [{"id": filme.id, "titulo": filme.titulo, "genero": filme.genero, "duracao": filme.duracao} for filme in filmes]
    
    return jsonify(filmes_list)

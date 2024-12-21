from flask import Flask
from models import db, Filme
from flask_cors import CORS

# Importando os blueprints
from routes.home import home_bp
from routes.filmes import filmes_bp
from routes.reservas import reservas_bp

# Inicializando o Flask
app = Flask(__name__)

CORS(app)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cinema.db'
db.init_app(app)  # Inicializando o banco de dados com o app Flask

# Registrando os blueprints
app.register_blueprint(home_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(reservas_bp)

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)

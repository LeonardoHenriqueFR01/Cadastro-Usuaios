from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializando o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializando o db com o app
    db.init_app(app)

    # Registrar as rotas
    from app.routes import register_routes
    register_routes(app)

    return app

from flask import render_template, request
from app import app

# Rota para página principal
def configure_routes(app):
    @app.route("/")
    def home():
        return render_template('index.html')



# Rota para pegar dados de formulário
def Formulario(app):
    @app.route('/submit', methods=['POST'])
    def submit():
        pass
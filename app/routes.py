from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from app import db
from app.models import User
import pandas as pd

def register_routes(app):
    # Rota para a página principal
    @app.route("/")
    def home():
        return render_template('index.html')

    # Rota para a página de login
    @app.route("/login")
    def pag_login():
        return render_template('login.html')

    # Rota para verificar dados de login
    @app.route("/submit-login", methods=["POST"])
    def submit_login():
        email = request.form.get('email')
        password = request.form.get('password')
        return redirect(url_for('pag_login'))

    # Rota para cadastrar um novo usuário
    @app.route("/submit-cadastro", methods=["POST"])
    def submit_cadastro():
        email = request.form.get('email')
        password = request.form.get('password')

        # Hashing da senha
        hashed_password = generate_password_hash(password)

        # Criar um DataFrame temporário (apenas para visualização ou manipulação de dados)
        user_data = {'email': [email], 'password': [hashed_password]}
        df = pd.DataFrame(user_data)

        # Exibir o DataFrame para ver os dados
        print(df)

        # Salvar no banco de dados
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return f"Cadastro finalizado! Email: {email}"

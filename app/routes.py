from app import app
from flask import render_template, url_for, request

# Rota par página principal do projeto
@app.route("/")
def home():
    return render_template('index.html')


# Rota para verificar dados de login
@app.route("/submit-login", methods=["POST"])
def submit_login():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Login Bem-Vindo de volta Email: {email} password: {password}"


# Rota para verificar dados de cadastro
@app.route("/submit-cadastro", methods=['POST'])
def submit_cadastro():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Cadastro finalizado Email: {email} password: {password}"

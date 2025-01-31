from flask import render_template, redirect, url_for, request
from app import app

# Página inicial
@app.route("/")
def home():
    return render_template('index.html', message=None, message_type=None)

# Página após login bem-sucedido
@app.route("/login")
def Login_Sucess():
    u_name = request.args.get('u_name')
    u_email = request.args.get('u_email')
    return render_template('sucess_login.html', name=u_name, email=u_email)

# Página após cadastro bem-sucedido
@app.route("/cadastro")
def Cadastro_Sucess():
    name = request.args.get('u_name')
    email = request.args.get('u_email')
    return render_template('sucess_cadastro.html', name=name, email=email)

@app.route('/submit', methods=['POST'])
def submit():
    form_type = request.form.get('form_type')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    message = None
    message_type = None

    if form_type == 'cadastro':
        # Salva os dados do usuário
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{name},{email},{password}\n")
        
        message = 'Cadastro realizado com sucesso!'
        message_type = 'success'
        return render_template('index.html', message=message, message_type=message_type)

    elif form_type == 'login':
        try:
            with open('usuarios.txt', 'r') as arquivo:
                usuarios = arquivo.readlines()

            for usuario in usuarios:
                u_name, u_email, u_password = usuario.strip().split(',')
                
                if email == u_email and password == u_password:
                    message = 'Login realizado com sucesso!'
                    message_type = 'success'
                    return render_template('sucess_login.html', name=u_name, email=u_email)

        except FileNotFoundError:
            message = 'Nenhum usuário cadastrado ainda!'
            message_type = 'error'
            return render_template('index.html', message=message, message_type=message_type)

        message = 'Email ou senha inválidos!'
        message_type = 'error'
        return render_template('index.html', message=message, message_type=message_type)

    message = 'Ação inválida!'
    message_type = 'error'
    return render_template('index.html', message=message, message_type=message_type)

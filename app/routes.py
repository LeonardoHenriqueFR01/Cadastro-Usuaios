from flask import render_template, redirect, url_for, request, jsonify
from app import app


# Rota para página principal
@app.route("/")
def home():
    return render_template('index.html')


# Rota para paǵina após fazer login
@app.route("/login")
def Login_Sucess():
    # Obtém os dados da URL
    u_name = request.args.get('u_name')
    u_email = request.args.get('u_email')
    return render_template('sucess_login.html', name=u_name, email=u_email)


# Rota para página após fazer cadastro
@app.route("/cadastro")
def Cadastro_Sucess():
    # Obtém os dados da URL
    name = request.args.get('u_name')
    email = request.args.get('u_email')
    return render_template('sucess_cadastro.html', name=name, email=email)


# Rota para pegar dados do formulário
@app.route('/submit', methods=['POST'])
def submit():
    # Obtém o valor de 'form_type' para diferenciar cadastro de login
    form_type = request.form.get('form_type')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if form_type == 'cadastro':
        # Lógica de cadastro
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{name},{email},{password}\n")
        return redirect(url_for('Cadastro_Sucess', u_name=name, u_email=email))


    elif form_type == 'login':
        # Lógica de login
        try:
            with open('usuarios.txt', 'r') as arquivo:
                usuarios = arquivo.readlines()
            for usuario in usuarios:
                u_name, u_email, u_password = usuario.strip().split(',')
                if email == u_email and password == u_password:
                    # Passa os dados como parâmetros de consulta
                    return redirect(url_for('Login_Sucess', u_name=u_name, u_email=u_email))
            return jsonify({"message": "Credenciais inválidas!"}), 401
        except FileNotFoundError:
            return jsonify({"message": "Nenhum usuário cadastrado ainda!"}), 404

    return jsonify({"message": "Ação inválida!"}), 400

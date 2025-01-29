// Função para gerar interface de login
function login() {
    
    // Pegando a interface de cadastro
    const cadastro = document.getElementById('cadastro')
    
    // Pegando a interface de login
    const login = document.getElementById('login')

    // Desabilitando a interface de cadastro
    cadastro.style.display = 'none'

    // Habilitando a interface de login
    login.style.display = 'block'

}

// Função para gerar interface de cadastro
function cadastro() {
    
    // Pegando a interface de cadastro
    const cadastro = document.getElementById('cadastro')
    
    // Pegando a interface de login
    const login = document.getElementById('login')

    // Desabilitando a interface de login
    login.style.display = 'none'

    // Habilitando a interface de cadastro
    cadastro.style.display = 'block'

}
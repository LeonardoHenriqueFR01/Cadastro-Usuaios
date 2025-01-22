
// Função para exibir o formulário de cadastro
function cadastrar() {
    var login = document.getElementById('login')
    var cadastro = document.getElementById('cadastro')

    // Oculta a interface de login
    login.style.display = 'none'
    
    // Exibe a interface de cadastro
    cadastro.style.display = 'flex'
    cadastro.style.alignItems = 'center'
}

// Função para exibir o formulário de login
function login() {
    var login = document.getElementById('login')
    var cadastro = document.getElementById('cadastro')

    // Oculta a interface de cadasto
    cadastro.style.display = 'none'

    // Exibe a interface de login
    login.style.display = 'flex'
    login.style.alignItems = 'center'
}

// ===== VALIDAÇÕES DE FORMULÁRIO =====

// Login
function validarLoginESeguir(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value.trim();
    const senha = document.getElementById('senha').value.trim();
    
    if (!email || !senha) {
        alert('Por favor, preencha todos os campos');
        return false;
    }
    
    if (!validarEmail(email)) {
        alert('Por favor, insira um email válido');
        return false;
    }
    
    window.location.href = "../../.";
    /* Volta algumas partes do caminho escritos na url até chegar na página principal 
    ex: 127.0.0.1:8000/usuario/entrar/ 
    -> 127.0.0.1:8000 */
}

// Signin
function validarSigninESeguir(event) {
    event.preventDefault();
    
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const nascimento = document.getElementById('nascimento').value.trim();
    const senha = document.getElementById('senha').value.trim();
    const confirmPassword = document.getElementById('confirm_password').value.trim();
    
    if (!nome || !email || !nascimento || !senha || !confirmPassword) {
        alert('Por favor, preencha todos os campos');
        return false;
    }
    
    if (!validarEmail(email)) {
        alert('Por favor, insira um email válido');
        return false;
    }
    
    if (senha !== confirmPassword) {
        alert('As senhas não coincidem');
        return false;
    }
    
    if (senha.length < 6) {
        alert('A senha deve ter no mínimo 6 caracteres');
        return false;
    }
    
    window.location.href = "emocoes1/";
}

// Renda
function validarRendaESeguir(event) {
    event.preventDefault();
    
    const profissao = document.getElementById('profissão').value.trim();
    const renda = document.getElementById('renda').value.trim();
    const fonteRenda = document.getElementById('fonte-renda').value.trim();
    
    if (!profissao || !renda || !fonteRenda) {
        alert('Por favor, preencha todos os campos');
        return false;
    }
    
    if (isNaN(renda) || renda <= 0) {
        alert('Por favor, insira um valor de renda válido');
        return false;
    }
    
    window.location.href = "../../../."; 
    /* Volta algumas partes do caminho escritos na url até chegar na página principal 
    ex: 127.0.0.1:8000/usuario/se-cadastrar/renda/ 
    -> 127.0.0.1:8000 */
}

// Emoção Quest 01
function validarEmocao01ESeguir(event) {
    event.preventDefault();
    
    const emocoes = document.querySelectorAll('input[name="emocoes"]:checked');
    
    if (emocoes.length === 0) {
        alert('Por favor, selecione pelo menos uma emoção');
        return false;
    }
    
    window.location.href = "../emocoes2";
}

// Emoção Quest 02
function validarEmocao02ESeguir(event) {
    event.preventDefault();
    
    const frase = document.getElementById('frase').value;
    
    if (!frase) {
        alert('Por favor, selecione uma opção');
        return false;
    }
    
    window.location.href = "../saldo";
}

// Função auxiliar de validação de email
function validarEmail(email) {
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regexEmail.test(email);
}

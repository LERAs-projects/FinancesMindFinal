from django.shortcuts import render

# Accounts (login and sign up)
def login(request):
    return render(request, "usuario/login_cadastro/login.html")

def resetPassword(request):
    return render(request, "usuario/login_cadastro/reset_password.html")

def signin(request):
    return render(request, "usuario/login_cadastro/signin.html")

def perguntasEmocoes1(request):
    return render(request, "usuario/login_cadastro/emotion_quest01.html")

def perguntasEmocoes2(request):
    return render(request, "usuario/login_cadastro/emotion_quest02.html")

def perguntasSaldo(request):
    return render(request, "usuario/login_cadastro/saldo.html")

def perguntasRenda(request):
    return render(request, "usuario/login_cadastro/renda_inf.html")

def logout(request):
    return render(request, "usuario/login_cadastro/logout.html")

# perfil:
def perfil_view(request):
    return render(request, "usuario/perfil.html")

# análise:
def analise_view(request):
    return render(request, "usuario/analise.html") 
from django.urls import path, include
from .views import *

app_name = 'usuario'

urlpatterns = [
    # LOGIN / SIGNIN
    path('entrar/', login, name='login'),
    path('redefinir-senha/', resetPassword, name='resetPassword'),
    path('se-cadastrar/', signin, name='signin'),
    path('se-cadastrar/emocoes1/', perguntasEmocoes1, name='perguntasEmocoes1'),
    path('se-cadastrar/emocoes2/', perguntasEmocoes2, name='perguntasEmocoes2'),
    path('se-cadastrar/saldo/', perguntasSaldo, name='perguntasSaldo'),
    path('se-cadastrar/renda/', perguntasRenda, name='perguntasRenda'),
    path('sair/', logout, name='logout'),

    # PERFIL
    path('perfil/', perfil_view, name='perfil'), # precisará do ID depois

    # ANALISE
    path('analise/', analise_view, name='analise'), # precisará do ID depois e outro para criar análise, por exemplo.
]


from django.urls import path, include
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('entrar/', login, name='login'),
    path('redefinir-senha/', resetPassword, name='resetPassword'),
    path('se-cadastrar/', signin, name='signin'),
    path('se-cadastrar/emocoes1/', perguntasEmocoes1, name='perguntasEmocoes1'),
    path('se-cadastrar/emocoes2/', perguntasEmocoes2, name='perguntasEmocoes2'),
    path('se-cadastrar/saldo/', perguntasSaldo, name='perguntasSaldo'),
    path('se-cadastrar/renda/', perguntasRenda, name='perguntasRenda'),
    path('sair/', logout, name='logout'),

    path('nova-despesa/', novaDespesa, name='nova_despesa'),
    path('nova-receita/', novaReceita, name='nova_receita'),
    path('nova-transferencia/', novaTransferencia, name='nova_transferencia')
]
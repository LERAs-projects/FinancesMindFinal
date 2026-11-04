from django.urls import path, include
from .views import *

urlpatterns = [
    path('nova-despesa/', novaDespesa, name='nova_despesa'),
    path('nova-receita/', novaReceita, name='nova_receita'),
    path('nova-transferencia/', novaTransferencia, name='nova_transferencia')
]
from django.shortcuts import render

# Create your views here.

def novaDespesa(request):
    return render(request, 'usuario/transacoes/nova_despesa.html')

def novaTransferencia(request):
    return render(request, 'usuario/transacoes/nova_transferencia.html')

def novaReceita(request):
    return render(request, 'usuario/transacoes/nova_receita.html')

def verDiario(request):
    pass

def registroEmocao(request):
    pass


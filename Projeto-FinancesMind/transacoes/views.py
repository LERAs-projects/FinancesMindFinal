from django.shortcuts import render

# Create your views here.
def novaDespesa(request):
    return render(request, 'transacoes/nova_despesa.html')

def novaTransferencia(request):
    return render(request, 'transacoes/nova_transferencia.html')

def novaReceita(request):
    return render(request, 'transacoes/nova_receita.html')

def historico(request):
    return render(request, 'transacoes/historico.html')
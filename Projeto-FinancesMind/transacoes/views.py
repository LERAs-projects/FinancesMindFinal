from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .forms import *

# Create your views here.
def novaDespesa(request):

    today = timezone.localdate()
    yesterday = today - timedelta(days=1)

    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user      
            despesa.save()
            return redirect('home')
    else:
        form = DespesaForm()
        
    return render(request, 'transacoes/nova_despesa.html', {'form': form, 'today': today, 'yesterday': yesterday})

def novaReceita(request):

    today = timezone.localdate()
    yesterday = today - timedelta(days=1)
    
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            Receita.objects.create(
                valor=valor
            )
            return redirect('home')
    else:
        form = Receita()
    return render(request, 'transacoes/nova_receita.html', {'form': form, 'today': today, 'yesterday': yesterday})

def historico(request):
    return render(request, 'transacoes/historico.html')
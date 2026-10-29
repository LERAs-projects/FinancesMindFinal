from django.shortcuts import render

# Create your views here.

def home(request):
    #usuario = request.user
    #despesas = usuario.despesas.all()
    #receitas = usuario.receitas.all()

    return render(request, 'core/index.html')
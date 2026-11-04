from django.shortcuts import render


def diario_view(request):
    return render(request, 'diario/diario.html')
from django import forms
from .models import *

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['valor', 'categoria', 'lancamento', 'data', 'emocao', 'descricao']
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'lancamento': forms.RadioSelect,
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'emocao': forms.RadioSelect,
            'descricao': forms.TextInput(attrs={'class': 'form-control'})
        }

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['valor', 'lancamento', 'data', 'emocao', 'descricao']
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'lancamento': forms.RadioSelect,
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'emocao': forms.RadioSelect,
            'descricao': forms.TextInput(attrs={'class': 'form-control'})
        }
from django.urls import path
from .views import *

app_name = 'diario'

urlpatterns = [
    path('', diario_view, name='diario'),
]
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Usuario

# Para Admin:
class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("email", "nome", "data_nascimento")


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = "__all__"
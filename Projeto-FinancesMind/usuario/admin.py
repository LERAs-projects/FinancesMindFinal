from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    
    list_display = ("email", "nome", "is_staff")
    search_fields = ("email", "nome")
    ordering = ("nome",)

    fieldsets = (
        (None, {"fields": ["email"]}),
        (("Personal info"), {"fields": ("nome", "data_nascimento", "saldo", "profissao", "renda_mensal",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email","nome", "data_nascimento", "password1", "password2"),
            },
        ),
    )

admin.site.register(Usuario, UsuarioAdmin)
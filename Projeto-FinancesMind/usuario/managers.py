from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório.")
        email = self.normalize_email(email).lower() #lower porque a verificação será feita com o e-mail em lowercase.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # using=self._db diz para usar o banco especificado (se foi especificado, se não, usa o default) - Serve para projetos multibancos.
        # Em suma, using=self._db não é necessário para esse projeto (no estado atual)
        return user

    def create_user(self, email, password=None, **extra_fields):
        #Adicionando o campo "is_staff" com o valor False no extra_fields:
        #No entanto, setdefault só adiciona se ainda não tiver sido definido anteriormente, nos argumentos.
        extra_fields.setdefault("is_staff", False) 
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Caso alguém passe explicitamente is_staff ou is_superuser como False:
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário precisa de is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário precisa de is_superuser=True.")
        return self._create_user(email, password, **extra_fields)

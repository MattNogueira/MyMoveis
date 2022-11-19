from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Usuario(AbstractBaseUser):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    #editei a field de email e adicionei:
    USERNAME_FIELD = 'email'
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    @property
    def senha(self):
        return self.password

    def __str__(self):
        return self.nome

class Anunciante(Usuario):
    TIPOPESSOA_CHOICES = (
        (u'F', u'Física'),
        (u'J', u'Jurídica'),
    )
    tipoPessoa = models.CharField(
        max_length=1,
        choices = TIPOPESSOA_CHOICES,
        default='F')
    
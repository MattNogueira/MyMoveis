from django.db import models

class Usuario(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)

class Anunciante(Usuario):
    TIPOPESSOA_CHOICES = (
        (u'F', u'Física'),
        (u'J', u'Jurídica'),
    )
    tipoPessoa = models.CharField(max_length=8)
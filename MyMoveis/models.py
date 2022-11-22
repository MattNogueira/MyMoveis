from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Imovel(models.Model):
    TIPOIMOVEL_CHOICES = (
        (u'ED',u'Edícula'),
        (u'SO',u'Sobrado'),
        (u'AP',u'Apartamento'),
        (u'KT',u'Kitnet'),
        (u'FL',u'Flat'),
        (u'LO',u'Loft'),
        (u'SU',u'Studio'),
        (u'SI',u'Sítio'),
    )
    STATUSNEGOCIO_CHOICES = (
        (u'V',u'Compra/Venda'),
        (u'A',u'Aluguel')
    )
    tipo = models.CharField(max_length=2, choices=TIPOIMOVEL_CHOICES)
    mobiliado = models.BooleanField()
    cep = models.CharField(max_length=7)
    regrasuso = models.TextField()
    preco = models.FloatField()
    vagaest = models.IntegerField()
    endereco = models.CharField
    status = models.CharField(max_length=1, choices=STATUSNEGOCIO_CHOICES)
    anunciante = models.ForeignKey('Anunciante', on_delete=models.CASCADE, related_name='AnuncianteAnunciaImovel')

class Quarto(models.Model):
    moradores = models.IntegerField()
    desc = models.TextField()
    preco = models.FloatField()
    vagast = models.IntegerField()
    imovel = models.ForeignKey(Imovel, on_delete=models.RESTRICT)
    anunciante = models.ForeignKey('Anunciante', on_delete=models.CASCADE, related_name='AnucianteAnunciaQuarto')

class Usuario(AbstractBaseUser):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    #editei a field de email e adicionei:
    USERNAME_FIELD = 'email'
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    quarto = models.ForeignKey(Quarto, on_delete=models.SET_NULL, null=True, related_name='UsuarioAlugaQuarto')

    @property
    def senha(self):
        return self.password

    def __str__(self):
        return self.nome

    @property
    def nomecomp(self):
        return '%s %s' % (self.nome, self.sobrenome)

class Anunciante(Usuario):
    TIPOPESSOA_CHOICES = (
        (u'F', u'Física'),
        (u'J', u'Jurídica'),
    )
    tipoPessoa = models.CharField(
        max_length=1,
        choices = TIPOPESSOA_CHOICES,
        default='F')
    numddd = models.CharField(max_length=2)
    numparc = models.CharField(max_length=9)

    #Não sei se precisa, mas coloquei uma função que retorna o número de celular
    @property
    def celstr(self):
        return f'({self.numddd}) {self.numparc}'

from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def redSenha(request):
    return render(request, 'usuario/redefinir senha.html')
<<<<<<< HEAD
=======

def anunciante(request):
    return render(request, 'auth/anunciante.html')
>>>>>>> 9accebba09d559ed45c10090d1fdcdad3907feaa

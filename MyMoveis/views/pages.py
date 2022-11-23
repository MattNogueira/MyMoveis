from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def redSenha(request):
    return render(request, 'usuario/redefinir senha.html')

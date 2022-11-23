from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        ut = 'Bem Vindo,' + f'{request.usuario.nome}!'
    else:
        ut = 'Login'
    return render(request, 'pages/home.html', {
        'usertext':ut
    })

def redSenha(request):
    return render(request, 'usuario/redefinir senha.html')

def anunciante(request):
    return render(request, 'auth/anunciante.html')
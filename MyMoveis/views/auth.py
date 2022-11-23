from django.contrib import auth
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from MyMoveis.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean_password(self):
        return make_password(self.cleaned_data['password'])

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput, max_length=50)
    senha = forms.CharField(widget=forms.PasswordInput)

def login(request):
    frm = LoginForm(request.POST or None)

    if frm.is_valid():
        usuario = auth.authenticate(request, email = frm.cleaned_data['email'], senha=frm.cleaned_data['senha'])

        if usuario is not None:
            auth.login(request, usuario)
            return redirect('home')
        else:
            frm.add_error(None, 'Usuário ou senha inválidos')

    return render(request, 'auth/login.html', {
        'frm':  frm
    })

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):

    frm = UsuarioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('login')

    return render(request, 'auth/cadastro.html',{
        'frm':frm
    })

def anunciante(request):
    return render(request, 'auth/anunciante.html')

from django.contrib import auth
from django import forms
from django.shortcuts import redirect, render

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
            frm.add_error(None, 'Email ou senha inválidos.')

    return render(request, 'auth/login.html', {
        'frm':  frm
    })

def logout(request):
    auth.logout(request)
    return redirect('home')
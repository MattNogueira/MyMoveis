from django import forms
from MyMoveis.models import Usuario
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean_password(self):
        return make_password(self.cleaned_data['password'])

def cadastro(request):

    frm = UsuarioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('login')

    return render(request, 'usuario/cadastro.html',{
        'frm':frm
    })

def update(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    frm = UsuarioForm(request.POST or None, instance=usuario)

    if frm.is_valid():
        frm.save()
        return redirect('pages/home.html')
    
    return render(request, 'usuario/cadastro.html', {
        'frm': frm,
    })

def delete(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()
    return redirect('login')
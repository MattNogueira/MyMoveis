from django import forms
from MyMoveis.models import Anunciante
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

class AnuncianteForm(ModelForm):
    class Meta:
        model = Anunciante
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean_password(self):
        return make_password(self.cleaned_data['password'])

def cadastro(request):

    frm = AnuncianteForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('home')

    return render(request, 'anunciante/anunciante.html',{
        'frm':frm
    })

def update(request, id):
    anunciante = get_object_or_404(Anunciante, pk=id)
    frm = AnuncianteForm(request.POST or None, instance=anunciante)

    if frm.is_valid():
        frm.save()
        return redirect('pages/home.html')
    
    return render(request, 'anunciante/anunciante.html', {
        'frm': frm,
    })

def delete(request, id):
    anunciante = get_object_or_404(Anunciante, pk=id)
    anunciante.delete()
    return redirect('login')
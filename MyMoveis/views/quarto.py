from django.shortcuts import render, redirect, get_object_or_404
from MyMoveis.models import Quarto
from django.forms import ModelForm

class QuartoForm(ModelForm):
    class Meta:
        model = Quarto
        fields = '__all__'

def lista(request):
    return render(request, 'pages/anuncios.html', {
        'quartos': Quarto.objects.all()
    })

def insert(request):
    frm = QuartoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('quartos.lista')
    
    return render(request, 'quarto/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Quarto'
    })

def update(request, id):
    quarto = get_object_or_404(Quarto, pk=id)
    frm = QuartoForm(request.POST or None, instance=quarto)

    if frm.is_valid():
        frm.save()
        return redirect('quartos.lista')
    
    return render(request, 'quartos/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Quarto'
    })

def delete(request, id):
    quarto = get_object_or_404(Quarto, pk=id)
    quarto.delete()
    return redirect('quartos.lista')
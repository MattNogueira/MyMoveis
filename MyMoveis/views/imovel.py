from django.shortcuts import render, redirect, get_object_or_404
from MyMoveis.models import Imovel
from django.forms import ModelForm

class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'

def lista(request):
    return render(request, 'pages/anuncios.html', {
        'imoveis': Imovel.objects.all()
    })

def insert(request):
    frm = ImovelForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('imoveis.lista')
    
    return render(request, 'imovel/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Imovel'
    })

def update(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    frm = ImovelForm(request.POST or None, instance=imovel)

    if frm.is_valid():
        frm.save()
        return redirect('imoveis.lista')
    
    return render(request, 'imoveis/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Imovel'
    })

def delete(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    imovel.delete()
    return redirect('imoveis.lista')
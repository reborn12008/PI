from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from keycode.source.models import Curso as curso
from keycode.source.models import Uc as uc
from keycode.source.models import Tipo_utilizador as tipo_utilizador
from keycode.source.models import Utilizador as utilizador
from keycode.source.models import Sala as sala
from keycode.source.models import Horario as horario
from keycode.source.models import Acesso as acesso
from django import forms
from .forms import createRoomModelForm

TIPOS_SALA=[(0,'Laboratório'),(1,'Auditório'),(2,'Normal')]

def espaco(request):
    salas=[]


    for entry in sala.objects.all():
        print(entry)
        if entry.status == True:
            array=[entry.nome,entry.piso,entry.lotacao,entry.tipo,'Disponivel']
        else:
            array=[entry.nome,entry.piso,entry.lotacao,entry.tipo,'Indisponivel']
        salas.append(array)
    return render(request,'espaco.html',{'salas':salas})

def editar_espaco(request, nome):
    obj = get_object_or_404(sala, nome=nome)
    r = obj.nome
    form = createRoomModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('espaco')

    return render(request, 'editar_espaco.html', {'formulary':form,'nome_sala':r} )

def adicionar_espaco(request):
    form = createRoomModelForm(request.POST or None)

    if(request.method=="POST"):
        if form.is_valid():
            obj = form.save(commit=False)
            
            obj.save()
            form = createRoomModelForm()
            return redirect('espaco')
    return render(request, 'adicionar_espaco.html', { 'form': form })

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from keycode.source.models import Curso as curso
from keycode.source.models import Uc as uc
from keycode.source.models import Tipo_utilizador as tipo_utilizador
from keycode.source.models import Utilizador as utilizador
from keycode.source.models import Sala as sala
from keycode.source.models import Horario as horario
from keycode.source.models import Acesso as acesso
from django import forms
from .forms import createRoomForm, editRoomModelForm

TIPOS_SALA=[(0,'Laboratório'),(1,'Auditório'),(2,'Normal')]

piso_edicao=0
lotacao_edicao=0
lab_edicao=False
aud_edicao=False




def espaco(request):
    salas=[]

    for entry in sala.objects.all():
        if entry.laboratorio==True:
            if entry.status == True:
                array=[entry.nome,entry.piso,entry.lotacao,'Laboratório','Disponivel']
            else:
                array=[entry.nome,entry.piso,entry.lotacao,'Laboratório','Indisponivel']
        elif entry.auditorio==True:
            if entry.status == True:
                array=[entry.nome,entry.piso,entry.lotacao,'Auditório','Disponivel']
            else:
                array=[entry.nome,entry.piso,entry.lotacao,'Auditório','Indisponivel']
        else:
            if entry.status == True:
                array=[entry.nome,entry.piso,entry.lotacao,'Normal','Disponivel']
            else:
                array=[entry.nome,entry.piso,entry.lotacao,'Normal','Indisponivel']
        salas.append(array)
    return render(request,'espaco.html',{'salas':salas})

def editar_espaco(request, nome):
    obj = get_object_or_404(sala, nome=nome)
    r = obj.nome
    form = editRoomModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        if 'edit' in request.POST:
            form.save()
            return render(request,'edicao_concluida.html')
        elif 'remove' in request.POST:
            sala.objects.filter(nome=nome).delete()
            return render(request, 'remocao_concluida.html')
    return render(request,'editar_espaco.html',{'formulary':form,'nome_sala':r} )


def adicionar_espaco(request):
    form = createRoomForm()
    return render(request,'adicionar_espaco.html',{'form':form})


def inserir_espaco(request):
    if(request.method=="POST"):
        form = createRoomForm(request.POST)
        if form.is_valid():
            nome_da_sala=form.cleaned_data['nome_sala']
            piso_da_sala = form.cleaned_data['piso_sala']
            lotacao_da_sala = form.cleaned_data['lotacao_sala']
            tipo_da_sala = form.cleaned_data['tipo_sala']
            status_da_sala = form.cleaned_data['status_sala']
            print('Nome da sala:', nome_da_sala, 'Piso-', piso_da_sala, 'lotacao_sala-', lotacao_da_sala, 'Tipo: ', tipo_da_sala, 'Sataus:',status_da_sala)
            if(status_da_sala == 0):
                if(tipo_da_sala == 0):
                    sala.objects.create(nome = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=True, auditorio=False, status=False).save()
                elif(tipo_da_sala == 1):
                    sala.objects.create(nome = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=True, status=False).save()
                else:
                    sala.objects.create(nome = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=False, status=False).save()
            elif(status_da_sala == 1):
                if(tipo_da_sala == 0):
                    sala.objects.create(nome = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=True, auditorio=False, status=True).save()
                elif(tipo_da_sala == 1):
                    sala.objects.create(nome = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=True, status=True).save()
                else:
                    sala.objects.create(nome = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=False, status=True).save()
    return render(request, 'base.html')
        


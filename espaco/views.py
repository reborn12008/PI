from django.shortcuts import render, get_object_or_404
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
        if entry.tipo==True:
            if entry.status == True:
                array=[entry.nome,entry.piso,entry.lotacao,'Laboratório','Disponivel']
            else:
                array=[entry.nome,entry.piso,entry.lotacao,'Laboratório','Indisponivel']
        elif entry.tipo==False:
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
    form = createRoomModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    return render(request,'editar_espaco.html',{'formulary':form,'nome_sala':r} )

def adicionar_espaco(request):
    form = createRoomModelForm(request.POST or None)

    if(request.method=="POST"):
        obj = form.save(commit=False)

        print("********************")
        print(obj)
        print("********************")

        # if(obj.status == 0):
        #     if(obj.tipo == 0):
        #         nova_sala = sala(nome = nome,
        #                             piso = piso, lotacao = lotacao,
        #                             laboratorio=True, auditorio=False, status=False)
        #         nova_sala.save()
        #     elif(obj.tipo == 1):
        #         nova_sala = sala(nome = nome,
        #                             piso = piso, lotacao = lotacao,
        #                             laboratorio=False, auditorio=True, status=False)
        #         nova_sala.save()
        #     else:
        #         nova_sala = sala(nome = nome,
        #                             piso = piso, lotacao = lotacao,
        #                             laboratorio=False, auditorio=False, status=False)
        #         nova_sala.save()

        # elif(obj.status == 1):
        #     if(obj.tipo == 0):
        #         nova_sala = sala(nome = nome,
        #                             piso = piso, lotacao = lotacao,
        #                             laboratorio=True, auditorio=False, status=True)
        #         nova_sala.save()
        #     elif(obj.tipo == 1):
        #         nova_sala = sala(nome = nome,
        #                             piso = piso, lotacao = lotacao,
        #                             laboratorio=False, auditorio=True, status=True)
        #         nova_sala.save()
        #     else:
        #         nova_sala = sala(nome = nome,
        #                             piso = piso, lotacao = lotacao,
        #                             laboratorio=False, auditorio=False, status=True)
        #         nova_sala.save()
        
        obj.save()
        form = createRoomModelForm()
    return render(request,'adicionar_espaco.html',{'form':form})

def inserir_espaco(request):

    if(request.method=="POST"):
        form = createRoomModelForm(request.POST)
        if form.is_valid():
            nome=form.cleaned_data['nome_sala']
            piso = form.cleaned_data['piso_sala']
            lotacao = form.cleaned_data['lotacao_sala']
            tipo = form.cleaned_data['tipo_sala']
            status_da_sala = form.cleaned_data['status_sala']
            if(status_da_sala == 0):
                if(tipo == 0):
                    nova_sala = sala(nome = nome,
                                     piso = piso, lotacao = lotacao,
                                     laboratorio=True, auditorio=False, status=False)
                    nova_sala.save()
                elif(tipo == 1):
                    nova_sala = sala(nome = nome,
                                     piso = piso, lotacao = lotacao,
                                     laboratorio=False, auditorio=True, status=False)
                    nova_sala.save()
                else:
                    nova_sala = sala(nome = nome,
                                     piso = piso, lotacao = lotacao,
                                     laboratorio=False, auditorio=False, status=False)
                    nova_sala.save()
            elif(status_da_sala == 1):
                if(tipo == 0):
                    nova_sala = sala(nome = nome,
                                     piso = piso, lotacao = lotacao,
                                     laboratorio=True, auditorio=False, status=True)
                    nova_sala.save()
                elif(tipo == 1):
                    nova_sala = sala(nome = nome,
                                     piso = piso, lotacao = lotacao,
                                     laboratorio=False, auditorio=True, status=True)
                    nova_sala.save()
                else:
                    nova_sala = sala(nome = nome,
                                     piso = piso, lotacao = lotacao,
                                     laboratorio=False, auditorio=False, status=True)
                    nova_sala.save()
    return render(request,'base.html')
        


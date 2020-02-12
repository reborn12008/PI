from django.shortcuts import render
from keycode.source.models import Curso as curso
from keycode.source.models import Uc as uc
from keycode.source.models import Tipo_utilizador as tipo_utilizador
from keycode.source.models import Utilizador as utilizador
from keycode.source.models import Sala as sala
from keycode.source.models import Horario as horario
from keycode.source.models import Acesso as acesso
from django import forms
from .forms import createRoomForm

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
                array=[entry.designacao_sala,entry.piso,entry.lotacao,'Laboratório','Disponivel']
            else:
                array=[entry.designacao_sala,entry.piso,entry.lotacao,'Laboratório','Indisponivel']
        elif entry.auditorio==True:
            if entry.status == True:
                array=[entry.designacao_sala,entry.piso,entry.lotacao,'Auditório','Disponivel']
            else:
                array=[entry.designacao_sala,entry.piso,entry.lotacao,'Auditório','Indisponivel']
        else:
            if entry.status == True:
                array=[entry.designacao_sala,entry.piso,entry.lotacao,'Normal','Disponivel']
            else:
                array=[entry.designacao_sala,entry.piso,entry.lotacao,'Normal','Indisponivel']
        salas.append(array)
    return render(request,'espaco.html',{'salas':salas})




class editForm(forms.Form):
    global piso_edicao
    global lotacao_edicao
    global lab_edicao
    global aud_edicao

    print(piso_edicao,'---',lotacao_edicao,'---',lab_edicao,'---',aud_edicao)
    piso = forms.IntegerField(required=True,label='Piso',widget=forms.NumberInput(attrs={'placeholder':piso_edicao}))
    lotacao = forms.IntegerField(required=True,label='Lotação',widget=forms.NumberInput(attrs={'placeholder':lotacao_edicao}))
    if (lab_edicao==True):
        tipo_sala = forms.ChoiceField(required=True,label='Tipo de Sala:',choices=TIPOS_SALA,initial = TIPOS_SALA[0])
    elif(aud_edicao==True):
        tipo_sala = forms.ChoiceField(required=True,label='Tipo de Sala:',choices=TIPOS_SALA,initial = TIPOS_SALA[1])
    else:
        tipo_sala = forms.ChoiceField(required=True,label='Tipo de Sala:',choices=TIPOS_SALA,initial = TIPOS_SALA[2])

    estado = forms.ChoiceField(required=True,label='Estado',choices=((0,'Indisponivel'),(1,'Disponivel')),initial = 1)


def editar_espaco(request):

    if(request.method=="GET"):
        global piso_edicao
        global lotacao_edicao
        global lab_edicao
        global aud_edicao
        r=request.GET['espaco_edit']
        for regist in sala.objects.all():
            if regist.designacao_sala == r :
                piso_edicao = regist.piso
                lotacao_edicao = regist.lotacao
                lab_edicao = regist.laboratorio
                aud_edicao = regist.auditorio
                print(piso_edicao,'---',lotacao_edicao,'---',lab_edicao,'---',aud_edicao)
                form = editForm()
                return render(request,'editar_espaco.html',{'formulary':form,'nome_sala':r} )
    return render(request,'espaco.html')

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
            if(status_da_sala == 0):
                if(tipo_da_sala == 0):
                    nova_sala = sala(designacao_sala = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=True, auditorio=False, status=False)
                    nova_sala.save()
                elif(tipo_da_sala == 1):
                    nova_sala = sala(designacao_sala = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=True, status=False)
                    nova_sala.save()
                else:
                    nova_sala = sala(designacao_sala = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=False, status=False)
                    nova_sala.save()
            elif(status_da_sala == 1):
                if(tipo_da_sala == 0):
                    nova_sala = sala(designacao_sala = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=True, auditorio=False, status=True)
                    nova_sala.save()
                elif(tipo_da_sala == 1):
                    nova_sala = sala(designacao_sala = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=True, status=True)
                    nova_sala.save()
                else:
                    nova_sala = sala(designacao_sala = nome_da_sala,
                                     piso = piso_da_sala, lotacao = lotacao_da_sala,
                                     laboratorio=False, auditorio=False, status=True)
                    nova_sala.save()
    return render(request,'base.html')
        


from django.shortcuts import render
from .forms import reservarForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def reservarView(request):
    if request.method == 'POST':
        form = reservarForm(request.POST)
        if(form.is_valid()):
            #receber os dados do formulário
            hora_inicial = form.cleaned_data['hora_inicial']
            minutos_inicial = form.cleaned_data['minutos_inicial']
            hora_final = form.cleaned_data['hora_final']
            minutos_final = form.cleaned_data['minutos_final']
            lotacao = form.cleaned_data['lotacao']
            laboratorio = form.cleaned_data['laboratorio']
            auditorio = form.cleaned_data['auditorio']
            if(laboratorio == True and auditorio==True):
                messages.warning(request,"Uma sala não pode ser laboratório e auditório simultaneamente!")
            if(validate_hours(hora_inicial,minutos_inicial,hora_final,minutos_final)):
                #TODO fazer Consulta,e display de vagas
                print("done")
            else:
                messages.warning(request,"A hora final deve ser superior à hora inicial")

        else:
            messages.warning(request,"Verifique os dados!")
    else:
        form = reservarForm()
    return render(request,'reservar.html', {'form': form})

def validate_hours(hora_inicial,minutos_inicial,hora_final,minutos_final):
  if(hora_inicial==hora_final):
    if(minutos_inicial>=minutos_final):
      return False
    else:
      return True
  else:
    if(hora_inicial<hora_final):
      return True
    else:
      return False

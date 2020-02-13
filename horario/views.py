from django.shortcuts import render
from keycode.source.models import Utilizador, Acesso

# Create your views here.

def horario(request):
    username = request.user
    current_user = Utilizador.objects.get(username=username)
    acessos = Acesso.objects.filter(utilizador=current_user.id)
    
    for acesso in acessos.iterator():
        print(acesso.utilizador.username)
        print(acesso.utilizador.tipo_utilizador)
        print(acesso.horario.sala.nome)
        print(acesso.horario.uc.nome_uc)
        print(acesso.horario.dia_semana)
        print(acesso.horario.hora_inicio)
        print(acesso.horario.hora_fim)

    return render(request,'horario.html')

from django.shortcuts import render
from keycode.source.models import Utilizador, Acesso

# Create your views here.

def horario(request):
    username = request.user
    current_user = Utilizador.objects.get(username=username)
    acesso = Acesso.objects.get(utilizador=current_user)

    print(acesso)

    return render(request,'horario.html')

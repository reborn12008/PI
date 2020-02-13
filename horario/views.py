from django.shortcuts import render
from keycode.source.models import Utilizador, Acesso

# Create your views here.

def horario(request):
    username = request.user
    print(username)
    current_user = Utilizador.objects.get(username=username)
    #acesso = Acesso.objects.get(utilizador=current_user.id)
    #for item in Acesso.objects.get(utilizador=current_user.id):
       # print(item[0].id)

    return render(request,'horario.html')

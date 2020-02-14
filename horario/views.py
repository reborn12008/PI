from django.shortcuts import render
from keycode.source.models import Utilizador, Acesso

# Create your views here.

def horario(request):
    username = request.user
    current_user = Utilizador.objects.get(username=username)
    acessos = Acesso.objects.filter(utilizador=current_user.id)

    aulas_nove = [None]*6
    aulas_dez = [None]*6
    aulas_onze = [None]*6
    aulas_doze = [None]*6
    aulas_treze = [None]*6
    aulas_quatorze = [None]*6
    aulas_quinze = [None]*6
    aulas_dezasseis = [None]*6
    aulas_dezassete = [None]*6
    aulas_dezoito = [None]*6
    aulas_dezanove = [None]*6
    aulas_vinte = [None]*6
    aulas_vum = [None]*6
    aulas_vdois = [None]*6
    aulas_vtres = [None]*6

    
    for acesso in acessos.iterator():
        #print(acesso.utilizador.username)
        #print(acesso.utilizador.tipo_utilizador)
        #print(acesso.horario.sala.nome)
        #print(acesso.horario.uc.nome_uc)
        #print(acesso.horario.dia_semana)
        #print(acesso.horario.hora_inicio)
        #print(acesso.horario.hora_fim)
        # COnverter os 2 primeiros digitos da string da hora inicial e final,subtrair para saber quantas vezes aparecerá aquela disciplina
        
        if( acesso.horario.hora_inicio == '09:30'):
            aulas_nove[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '10:30'): # or int(acesso.horario.hora_fim[:2])<11):
            aulas_dez[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '11:30' ): #or int(acesso.horario.hora_fim[:2])<12):
            aulas_onze[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '12:30'): # or int(acesso.horario.hora_fim[:2])<13):
            aulas_doze[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '13:30'): # or int(acesso.horario.hora_fim[:2])<14):
            aulas_treze[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '14:30'):
            aulas_quatorze[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '15:30'):
            aulas_quinze[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '16:30'):
            aulas_dezasseis[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '17:30'):
            aulas_dezassete[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '18:30'):
            aulas_dezoito[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '19:30'):
            aulas_dezanove[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '20:30'):
            aulas_vinte[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '21:30'):
            aulas_vum[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '22:30'):
            aulas_vdois[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc
        elif( acesso.horario.hora_inicio == '23:30'):
            aulas_vtres[acesso.horario.dia_semana-1] = acesso.horario.uc.nome_uc

    return render(request,'horario.html', {'aulas_nove' : aulas_nove, 'aulas_dez' : aulas_dez,
                                           'aulas_onze' : aulas_onze, 'aulas_doze' : aulas_doze,
                                           'aulas_treze' : aulas_treze, 'aulas_quatroze' : aulas_quatorze,
                                           'aulas_quinze' : aulas_quinze, 'aulas_dezaseis' : aulas_dezasseis,
                                           'aulas_dezasete' : aulas_dezassete, 'aulas_dezoito' : aulas_dezoito,
                                           'aulas_dezanove' : aulas_dezanove, 'aulas_vinte' : aulas_vinte,
                                           'aulas_vum' : aulas_vum,'aulas_vdois' : aulas_vdois,
                                           'aulas_vdois' : aulas_vdois, 'aulas_vtres' : aulas_vtres})

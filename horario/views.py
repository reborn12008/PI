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


    acessos_list = []
    for acesso in acessos.iterator():
        acessos_list.append(
            {
                'pincode' : acesso.pincode,
                'hora_inicio': acesso.horario.hora_inicio,
                'hora_fim': acesso.horario.hora_fim,
                'dia_semana': acesso.horario.dia_semana,
                'nome_uc': acesso.horario.uc.nome_uc,
                'sala': acesso.horario.sala.nome
            }
        )

    lista_expandida = []
    for acesso in acessos_list:
        dif_horas=int(acesso['hora_fim'][:2]) - int(acesso['hora_inicio'][:2])
        if dif_horas > 1: # (têm de arranjar maneira de fazer esta subtração, pesquisem como subtrair horas no google)
            acesso_expandido = converter_batch_de_horas(dif_horas,acesso['pincode'],acesso['hora_inicio'],acesso['hora_fim'],acesso['dia_semana'],acesso['nome_uc'],acesso['sala']) #(acesso_expandido vai ser uma lista)
            for item in acesso_expandido:
                lista_expandida.append(item)
        else:
            lista_expandida.append(acesso)

    for it in lista_expandida:
        #print(acesso.utilizador.username)
        #print(acesso.utilizador.tipo_utilizador)
        #print(acesso.horario.sala.nome)
        #print(acesso.horario.uc.nome_uc)
        #print(acesso.horario.dia_semana)
        #print(acesso.horario.hora_inicio)
        #print(acesso.horario.hora_fim)
        # COnverter os 2 primeiros digitos da string da hora inicial e final,subtrair para saber quantas vezes aparecerá aquela disciplina
        
        if( it['hora_inicio'] == '9:30'):
            aulas_nove[it['dia_semana']] = { 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '10:30'): 
            aulas_dez[it['dia_semana']] = { 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '11:30' ): 
            aulas_onze[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '12:30'): 
            aulas_doze[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '13:30'): 
            aulas_treze[it['dia_semana']] = {'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '14:30'):
            aulas_quatorze[it['dia_semana']] = { 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '15:30'):
            aulas_quinze[it['dia_semana']] = { 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '16:30'):
            aulas_dezasseis[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '17:30'):
            aulas_dezassete[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '18:30'):
            aulas_dezoito[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '19:30'):
            aulas_dezanove[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '20:30'):
            aulas_vinte[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '21:30'):
            aulas_vum[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '22:30'):
            aulas_vdois[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }
        elif( it['hora_inicio'] == '23:30'):
            aulas_vtres[it['dia_semana']] ={ 'nome_uc' : it['nome_uc'], 'sala' : it['sala'], 'pincode' : it['pincode'] }

    return render(request,'horario.html', {'aulas_nove' : aulas_nove, 'aulas_dez' : aulas_dez,
                                           'aulas_onze' : aulas_onze, 'aulas_doze' : aulas_doze,
                                           'aulas_treze' : aulas_treze, 'aulas_quatorze' : aulas_quatorze,
                                           'aulas_quinze' : aulas_quinze, 'aulas_dezaseis' : aulas_dezasseis,
                                           'aulas_dezasete' : aulas_dezassete, 'aulas_dezoito' : aulas_dezoito,
                                           'aulas_dezanove' : aulas_dezanove, 'aulas_vinte' : aulas_vinte,
                                           'aulas_vum' : aulas_vum,'aulas_vdois' : aulas_vdois,
                                            'aulas_vtres' : aulas_vtres})


def converter_batch_de_horas(dif_horas,pincode,hora_inicio,hora_fim,dia_semana,nome_uc,sala):
    bloco_horario = []
    hora_i=int(hora_inicio[:2])
    hora_f=hora_i + 1
    for i in range(dif_horas):
        bloco_horario.append(
            {
                'pincode' : pincode,
                'hora_inicio' : str(hora_i) + ':30',
                'hora_fim' : str(hora_f) + ':30',
                'dia_semana' : dia_semana - 1 ,
                'nome_uc' : nome_uc,
                'sala' : sala
            }
        )
        hora_i += 1
        hora_f = hora_i + 1     
    return bloco_horario
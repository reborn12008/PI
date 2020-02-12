from django import forms

class createRoomForm(forms.Form):
    nome_sala=forms.CharField(max_length=4,required=True,label = "Nome da Sala: ")
    piso_sala = forms.IntegerField(min_value=-1,max_value=2)
    lotacao_sala = forms.IntegerField(min_value=10,max_value=55,label = "Lotação Máxima")
    tipo_sala = forms.ChoiceField(choices=((0,'Laboratório'),(1,'Auditório'),(3,'Normal')),required=True, label = "Tipo")
    status_sala = forms.ChoiceField(choices=((0,'Indisponivel'),(1,'Disponivel')),required=True, label = "Disponibilidade",initial=1)

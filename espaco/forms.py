from django import forms

from keycode.source.models import Sala as sala

TIPOS_SALA=[(0,'Laboratório'),(1,'Auditório'),(2,'Normal')]

class createRoomForm(forms.Form):
    nome = forms.CharField(max_length=4,required=True,label = "Nome da Sala: ")
    piso = forms.IntegerField(min_value=-1,max_value=2)
    lotacao = forms.IntegerField(min_value=10,max_value=55,label = "Lotação Máxima")
    tipo = forms.ChoiceField(choices=((0,'Laboratório'),(1,'Auditório'),(3,'Normal')),required=True, label = "Tipo")
    status = forms.ChoiceField(choices=((0,'Indisponivel'),(1,'Disponivel')),required=True, label = "Disponibilidade",initial=1)

class createRoomModelForm(forms.ModelForm):
    class Meta:
        model = sala
        fields = ['nome', 'piso', 'lotacao', 'tipo', 'status']
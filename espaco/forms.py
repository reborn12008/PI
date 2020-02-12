from django import forms

from keycode.source.models import Sala as sala

TIPOS_SALA=[(0,'Laboratório'),(1,'Auditório'),(2,'Normal')]

class createRoomForm(forms.Form):
    nome_sala=forms.CharField(max_length=4,required=True,label = "Nome da Sala ")
    piso_sala = forms.IntegerField(min_value=-1,max_value=1, required=True)
    lotacao_sala = forms.IntegerField(min_value=10,max_value=55,required=True,label = "Lotação Máxima")
    tipo_sala = forms.ChoiceField(choices=((0,'Laboratório'),(1,'Auditório'),(2,'Normal')),required=True, label = "Tipo")
    status_sala = forms.ChoiceField(choices=((0,'Indisponivel'),(1,'Disponivel')),required=True, label = "Disponibilidade",initial=1)
            
class editRoomForm(forms.Form):
    nome = forms.CharField(max_length=4,required=True)
    piso = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'min': -1, 'max': 1}))
    lotacao = forms.IntegerField(required=True,widget=forms.NumberInput())
    tipo_sala = forms.ChoiceField(choices=((0, 'Laboratório'), (1, 'Auditório'), (2, 'Normal')), required=True,
                                  label="Tipo")
    status = forms.ChoiceField(required=True,label='Estado',choices=((0,'Indisponivel'),(1,'Disponivel')),initial = 1)

class editRoomModelForm(forms.ModelForm):
    class Meta:
        model = sala
        fields = ['nome', 'piso', 'lotacao', 'status']
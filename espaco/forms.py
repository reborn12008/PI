from django import forms

from keycode.source.models import Sala as sala

TIPO_SALA = [
    ("Auditorio", "Auditorio"),
    ("Laboratorio", "Laboratorio"),
    ("Normal", "Normal")
]

class createRoomForm(forms.Form):
    nome = forms.CharField(max_length=4,required=True,label = "Nome da Sala: ")
    piso = forms.IntegerField(min_value=-1,max_value=2)
    lotacao = forms.IntegerField(min_value=10,max_value=55,label = "Lotação Máxima")
    tipo = forms.CharField(widget=forms.SelectMultiple(choices=TIPO_SALA),required=True, label = "Tipo")
    status = forms.ChoiceField(choices=((0,'Indisponivel'),(1,'Disponivel')),required=True, label = "Disponibilidade",initial=1)

    def clean(self):
        cleaned_data = super().clean()
        lotacao = cleaned_data.get('lotacao')
        piso = cleaned_data.get('piso')
        if lotacao < 1 or lotacao > 55:
            raise forms.ValidationError("Erro: Lotação tem de ser positiva e até 55.")
        
        if piso < -1 or piso > 1:
            raise forms.ValidationError("Erro: Piso tem de ser entre -1 e 1.")
        return cleaned_data

class createRoomModelForm(forms.ModelForm):
    class Meta:
        model = sala
        fields = ['nome', 'piso', 'lotacao', 'tipo', 'status']
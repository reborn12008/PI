from django import forms

from keycode.source.models import Sala as sala

TIPO_SALA = [
    ("Auditorio", "Auditorio"),
    ("Laboratorio", "Laboratorio"),
    ("Normal", "Normal")
]

class createRoomForm(forms.Form):
    nome = forms.CharField(max_length=4,required=True)
    piso = forms.IntegerField(min_value=-1,max_value=2)
    lotacao = forms.IntegerField(min_value=10,max_value=55)
    tipo = forms.CharField(widget=forms.SelectMultiple(choices=TIPO_SALA),required=True)
    status = forms.ChoiceField(choices=((0,'Indisponivel'),(1,'Disponivel')),required=True,initial=1)

        
class createRoomModelForm(forms.ModelForm):
    class Meta:
        model = sala
        fields = ['nome', 'piso', 'lotacao', 'tipo', 'status']

    def clean_lotacao(self):
        cleaned_data = super().clean()
        lotacao = cleaned_data.get('lotacao')
    
        if lotacao < 1 or lotacao > 55:
            raise forms.ValidationError("Erro: Lotação tem de ser positiva e até 55.")
        
        return lotacao

    def clean_piso(self):
        cleaned_data = super().clean()
        piso = cleaned_data.get('piso')
        if piso < -1 or piso > 1:
            raise forms.ValidationError("Erro: Piso tem de ser entre -1 e 1.")

        return piso
from django import forms
from datetime import timedelta
import datetime
from django.core.exceptions import ValidationError

HOUR_CHOICES=(
    ("8","08"),
    ("9","09"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
    ("13","13"),
    ("14","14"),
    ("15","15"),
    ("16","16"),
    ("17","17"),
    ("18","18"),
    ("19","19"),
    ("20","20"),
    ("21","21"),
    ("22","22"),
    ("23","23"),


)
MIN_CHOICES =( 
    ("1", "00"), 
    ("2", "30"),
)

duracaomes=timedelta(days=30)

def valid_date(value):
  if(value<=datetime.date.today()):
    raise forms.ValidationError("A reserva tem de ser feita para uma data futura!")
  return value

class DateInput(forms.DateInput):
  input_type='date'

class reservarForm(forms.Form):
  data = forms.DateField(widget=DateInput, initial=datetime.date.today(),label='Data da Reserva',validators=[valid_date])
  hora_inicial = forms.ChoiceField(choices=HOUR_CHOICES)
  minutos_inicial = forms.ChoiceField(choices=MIN_CHOICES,label='')
  hora_final = forms.ChoiceField(choices=HOUR_CHOICES)
  minutos_final = forms.ChoiceField(choices=MIN_CHOICES,label='')
  lotacao= forms.IntegerField(min_value=1,max_value=68)
  laboratorio = forms.BooleanField(required=False)
  auditorio = forms.BooleanField(required=False)


class ExampleModelForm(forms.Form):
  class Meta:
    widgets = {'data' : DateInput()}



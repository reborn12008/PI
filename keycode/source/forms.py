from django import forms


class loginForm(forms.Form):
     username = forms.CharField(label='Username', widget= forms.TextInput(
          attrs = {
          'class' : 'col-md-12',
          }
     ))
     password = forms.CharField(label='Password', widget= forms.PasswordInput(
          attrs = {
               'class' : 'col-md-12',
          }
     ))

from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,label='E-mail de envio:')
    subject = forms.CharField(required=True,label='Assunto:')
    message = forms.CharField(widget=forms.Textarea, required=True,label='Menssagem:')

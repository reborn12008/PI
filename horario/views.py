from django.shortcuts import render

# Create your views here.

def horario(request):
    return render(request,'horario.html')

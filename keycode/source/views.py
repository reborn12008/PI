from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import loginForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def home(request):
    if request.method=='POST':
        form=loginForm(request.POST)
        if(form.is_valid()):
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            tryLogin=authenticate(request,username=username,password=password)
            login(request,tryLogin)
            return render(request,'base.html',{'user': username})
    else:
        form=loginForm()

    return render(request, 'base.html',{'form': form})

def contactosView(request):
    return render(request,'contactos.html')

@login_required
def logoutView(request):
    form=loginForm()
    logout(request)
    return render(request,'base.html',{'form': form})



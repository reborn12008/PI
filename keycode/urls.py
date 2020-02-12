"""keycode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from keycode.source import views as source_views
from sendemail import views as sendemail_views
from register import views as register_views
from reservar import views as reservar_views
from horario import views as horario_views
from reservar import views as reservar_views
from espaco import views as espaco_views


urlpatterns = [
    url(r'^$', source_views.home, name='home'),
    url(r'^sendemail/$',sendemail_views.emailView, name='reportarerro'),
    url(r'^reservar/$',reservar_views.reservarView, name='reservar'),
    url(r'^contactos/$',source_views.contactosView, name='contactos'),
    url(r'^logout/$', source_views.logoutView, name='logout'),
    url(r'^signup/$', register_views.signup, name='signup'),
    url(r'^horario/$', horario_views.horario, name='horario'),
    path('admin/', admin.site.urls),
    path('', include('sendemail.urls')),
    path('', include('espaco.urls')),
]

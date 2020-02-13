from django.contrib import admin
from django.urls import path

from .views import espaco,editar_espaco,adicionar_espaco

urlpatterns = [
    path('espaco/', espaco, name='espaco'),
    path('adicionar/', adicionar_espaco, name='adicionar_espaco'),
    path('editar/<str:nome>', editar_espaco, name='editar_espaco'),
]	

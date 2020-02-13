from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.

POR_USAR = 0
USADO = 1
STATUS_PIN = ((POR_USAR,'Off'),(USADO,'On'))

SEGUNDA = 1
TERCA = 2
QUARTA = 3
QUINTA = 4
SEXTA = 5
SABADO = 6
DIAS_SEMANA = ((SEGUNDA,'Segunda-feira'),(TERCA,'Terça-feira'),(QUARTA,'Quarta-Feira'),(QUINTA,'Quinta-feira'),(SEXTA,'Sexta-feira'),(SABADO,'Sábado'))

TIPO_SALA = [
    ("Auditorio", "Auditorio"),
    ("Laboratorio", "Laboratorio"),
    ("Normal", "Normal")
]

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_curso



class Uc(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome_uc = models.CharField(max_length=50)

    def __str__(self):
        return self.curso,self.nome_uc



class Tipo_utilizador(models.Model):
    nome_tipo_utilizador = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_tipo_utilizador



class Utilizador(models.Model):
    tipo_utilizador=models.ForeignKey(Tipo_utilizador, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True, blank=False)
    primeiro_nome_utilizador = models.CharField(max_length=50)
    ultimo_nome_utilizador = models.CharField(max_length=50)

    def __str__(self):
        return str(self.username, self.tipo_utilizador,self.primeiro_nome_utilizador,self.ultimo_nome_utilizador)

    class Meta:
        ordering = ['username']


class Sala(models.Model):
    nome = models.CharField(max_length=10, unique=True)
    piso = models.IntegerField()
    lotacao = models.IntegerField()
    tipo = models.CharField(max_length=25, choices=TIPO_SALA)
    status = models.BooleanField()

    def __str__(self):
        return str((self.nome, self.piso, self.lotacao, self.tipo, self.status))

    class Meta:
        ordering = ['-nome', '-lotacao']


class Horario(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    uc = models.ForeignKey(Uc, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.CharField(max_length=10)
    hora_fim = models.CharField(max_length=10)
    
    def __str__(self):
        return self.sala,self.uc,self.hora_inicio,self.hora_fim


class Acesso(models.Model):
    utilizador = models.ForeignKey(Utilizador,on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=20)
    pincode_status = models.SmallIntegerField(choices=STATUS_PIN)

    def __str__(self):
        return self.pincode



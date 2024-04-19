from django.db import models

class Reserva(models.Model):
    email = models.EmailField(default='')
    valor = models.IntegerField()
    lugar = models.CharField(max_length=3)
    comprado = models.BooleanField(default=False) 

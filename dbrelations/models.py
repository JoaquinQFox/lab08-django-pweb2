from django.db import models

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=10)

class Framework(models.Model):
    nombre = models.CharField(max_length=10)
    lenguaje = models.ForeignKey(Lenguaje, on_delete=models.CASCADE)
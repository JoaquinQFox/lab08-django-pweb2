from django.db import models

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Framework(models.Model):
    nombre = models.CharField(max_length=10)
    lenguaje = models.ForeignKey(Lenguaje, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    nombre = models.CharField(max_length=10)
    peliculas = models.ManyToManyField(Pelicula)

    def __str__(self):
        return self.nombre
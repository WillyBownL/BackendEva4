from django.db import models

# Create your models here.
class Concierto (models.Model):
    artista = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=50)
    cupo = models.IntegerField()
    #se agregan los 5 campos que se utilizaran para concierto

    def __str__(self):
        return f"{self.artista} - {self.fecha}"
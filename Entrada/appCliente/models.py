from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    rut = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
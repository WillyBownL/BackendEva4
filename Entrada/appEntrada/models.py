from django.db import models
from appCliente.models import cliente  # Importa el modelo Cliente desde appCliente
from appConcierto.models import Concierto  # Importa el modelo Concierto desde appConcierto

class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)  # Referencia a appCliente.Cliente
    id_concierto = models.ForeignKey(Concierto, on_delete=models.CASCADE)  # Referencia a appConcierto.Concierto
    precio = models.IntegerField()
    area_designada = models.CharField(max_length=50)
    fecha_reserva = models.DateField()

    

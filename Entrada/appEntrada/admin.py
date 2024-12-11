from django.contrib import admin
from appEntrada.models import Entrada

# Register your models here.
class EntradaAdmin(admin.ModelAdmin):
    list_display = ['id_cliente','id_concierto','precio','area_designada','fecha_reserva']

admin.site.register(Entrada, EntradaAdmin)

# admin 123

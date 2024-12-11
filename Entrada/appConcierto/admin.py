from django.contrib import admin
from appConcierto.models import Concierto


class ConciertoAdmin(admin.ModelAdmin):
    list_display = ['artista', 'fecha', 'hora', 'ubicacion', 'cupo']

# Register your models here.
admin.site.register(Concierto, ConciertoAdmin)

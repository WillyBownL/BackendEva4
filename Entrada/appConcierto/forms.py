from django import forms
from appConcierto.models import Concierto
from datetime import date, time
import re #regex



class FormConcierto(forms.ModelForm):
    #validar caracteres del nombre dek artista 
    def clean_artista(self):
        inputartista = self.cleaned_data['artista']
         #Validar que el nombre del artista no contenga más de 35 caracteres
        if len(inputartista) > 35 :
            raise forms.ValidationError("El nombre del artista no puede tener más de 35 carácteres.")
         #Validar que el nombre del artista no esté vacio
        if len(inputartista.strip()) == 0:
            raise forms.ValidationError("El nombre del artista no puede estar vacío.")
        return inputartista
    
    def clean_fecha(self):
        inputfecha = self.cleaned_data['fecha']
        # Validar que la fecha no esté en tiempo pasado
        if inputfecha < date.today():
            raise forms.ValidationError("La fecha del concierto no puede estar en el pasado.")
        return inputfecha
    
    def clean_hora(self):
        inputhora = self.cleaned_data['hora']
        # Validar que la hora esté dentro del rango permitido (18:00 - 03:00)
        if inputhora < time(18, 0) and inputhora > time(3, 0):
            raise forms.ValidationError("La hora del concierto debe estar entre las 18:00 y las 03:00.")
        return inputhora
    
    def clean_ubicacion(self):
        inputubicacion = self.cleaned_data['ubicacion']
        # Validar longitud máxima de la ubicación
        if len(inputubicacion) > 50:
            raise forms.ValidationError("La ubicación no puede tener más de 50 caracteres.")
        # Validar que no esté vacío el campo de la ubicación
        if len(inputubicacion.strip()) == 0:
            raise forms.ValidationError("La ubicación no puede estar vacía.")
        # Validar que solo contenga letras y espacios la ubicación
        if not re.match(r'^[a-zA-Z\s]+$', inputubicacion): #^->inicia la cadena, [a-zA-Z\s]->se refiere a solo letras y espacios, +-> que un caracter coincida con el anterior,$->final de la cadena
            raise forms.ValidationError("La ubicación solo puede contener letras y espacios.")
        return inputubicacion
    
    def clean_cupo(self):
        inputcupo = self.cleaned_data['cupo']
        # Validar que el cupo sea un entero positivo
        if inputcupo <= 0:
            raise forms.ValidationError("El cupo debe ser un número entero positivo.")
          # Validar que el cupo no sea igual a 0 ni mayor a 5.
        if inputcupo == 0:
            raise forms.ValidationError("El cupo no puede ser igual a cero.")
        if inputcupo > 5:
            raise forms.ValidationError("El cupo no puede ser mayor a cinco.")
        return inputcupo
    
    class Meta:
        model = Concierto
        fields = '__all__'


from django import forms
from appCliente.models import cliente  # Importa correctamente el modelo Cliente desde appCliente
from appConcierto.models import Concierto  # Importa correctamente el modelo Concierto desde appConcierto
from appEntrada.models import Entrada  # Asumiendo que Entrada es el modelo de la tabla en appEntrada
from datetime import date
import re  # regex

class FormEntrada(forms.ModelForm):

    # Validar el precio
    def clean_precio(self):
        inputprecio = self.cleaned_data['precio']
        # Validar que el campo no esté vacío
        if inputprecio is None or str(inputprecio).strip() == '':
            raise forms.ValidationError("El campo precio no puede estar vacío.")
        # Validar que el precio sea un número positivo
        try:
            inputprecio = float(inputprecio)
        except ValueError:
            raise forms.ValidationError("El precio debe ser un número válido.")
        # Validar que no sea un número negativo
        if inputprecio < 0:
            raise forms.ValidationError("El precio no puede ser un número negativo.")
        # Validar que no contenga caracteres especiales
        if not str(inputprecio).replace('.', '', 1).isdigit():  # Permite un solo punto decimal
            raise forms.ValidationError("El precio no puede contener caracteres especiales.")
        # Validar que el precio no sea excesivamente alto (esto es solo un ejemplo)
        if inputprecio < 50000:
            raise forms.ValidationError("El precio no puede ser menor a 50,000.")
        if inputprecio > 500000:
            raise forms.ValidationError("El precio no puede ser superior a 500,000.")
        return inputprecio

    # Validar el área designada
    def clean_area_designada(self):
        inputarea = self.cleaned_data['area_designada']
        # Validar que el campo no esté vacío
        if len(inputarea.strip()) == 0:
            raise forms.ValidationError("El área designada no puede estar vacía.")
        # Validar longitud máxima
        if len(inputarea) > 100:
            raise forms.ValidationError("El área designada no puede tener más de 100 caracteres.")
        # Validar que no contenga números
        if any(char.isdigit() for char in inputarea):
            raise forms.ValidationError("El área designada no puede contener números.")
        # Validar que no contenga caracteres especiales
        if not re.match(r'^[a-zA-Z\s]+$', inputarea):
            raise forms.ValidationError("El área designada solo puede contener letras y espacios.")
        return inputarea

    # Validar la fecha de reserva
    def clean_fecha_reserva(self):
        inputfecha_reserva = self.cleaned_data['fecha_reserva']
        
        # Validar que el campo no esté vacío
        if not inputfecha_reserva:
            raise forms.ValidationError("La fecha de reserva no puede estar vacía.")
        # Validar que la fecha no contenga caracteres especiales
        fecha_str = str(inputfecha_reserva)
        if not fecha_str.isdigit() and not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_str):  
            raise forms.ValidationError("La fecha de reserva no puede contener caracteres especiales.")
        # Validar que la fecha de reserva no esté en el pasado
        if inputfecha_reserva < date.today():
            raise forms.ValidationError("La fecha de reserva no puede estar en el pasado.")
        
        # Obtener la fecha del concierto desde el campo id_concierto
        concierto = self.cleaned_data.get('id_concierto')
        if concierto and inputfecha_reserva > concierto.fecha:
            raise forms.ValidationError("La fecha de reserva no puede ser posterior a la fecha del concierto.")
        
        return inputfecha_reserva

    class Meta:
        model = Entrada
        fields = ['id_cliente', 'id_concierto', 'precio', 'area_designada', 'fecha_reserva']
 
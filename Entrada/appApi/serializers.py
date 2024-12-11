from datetime import date, time
import re
from rest_framework import serializers
from appCliente.models import cliente
from appConcierto.models import Concierto
from appEntrada.models import Entrada

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= cliente
        fields= '__all__'


    def validate(self, data):
        inputTelefono = ['telefono']
        if not inputTelefono or len(str(inputTelefono)) != 9:
            raise serializers.ValidationError("El telefono debe tener un número válido (9 dígitos)")
        
        inputCorreo = ['correo']
        correo_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not inputCorreo or inputCorreo.find('@')== -1 or not re.match(correo_regex, inputCorreo):
            raise serializers.ValidationError("Ingrese un correo electrónico válido (formato: ejemplo@dominio.com)")
        
        inputRut = ['rut']
        rut_regex = r'^\d{7,8}-[0-9kK]$'
        if not re.match(rut_regex, inputRut) or not inputRut or len(inputRut) < 9 or len(inputRut) > 10 or inputRut.find('-')== -1:
            raise serializers.ValidationError("Ingrese un RUT válido (formato: XXXXXXXX-X)")

        return data

class ConciertoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Concierto
        fields= '__all__'

    def validate(self, data):

        inputartista = ['artista']
         #Validar que el nombre del artista no contenga más de 35 caracteres
        if len(inputartista) > 35 :
            raise serializers.ValidationError("El nombre del artista no puede tener más de 35 carácteres.")
         #Validar que el nombre del artista no esté vacio
        if len(inputartista.strip()) == 0:
            raise serializers.ValidationError("El nombre del artista no puede estar vacío.")

        inputfecha = ['fecha']
        # Validar que la fecha no esté en tiempo pasado
        if inputfecha < date.today():
            raise serializers.ValidationError("La fecha del concierto no puede estar en el pasado.")
        
        inputhora = ['hora']
        # Validar que la hora esté dentro del rango permitido (18:00 - 03:00)
        if inputhora < time(18, 0) and inputhora > time(3, 0):
            raise serializers.ValidationError("La hora del concierto debe estar entre las 18:00 y las 03:00.")
       

        inputubicacion = ['ubicacion']
        # Validar longitud máxima de la ubicación
        if len(inputubicacion) > 50:
            raise serializers.ValidationError("La ubicación no puede tener más de 50 caracteres.")
        # Validar que no esté vacío el campo de la ubicación
        if len(inputubicacion.strip()) == 0:
            raise serializers.ValidationError("La ubicación no puede estar vacía.")
        # Validar que solo contenga letras y espacios la ubicación
        if not re.match(r'^[a-zA-Z\s]+$', inputubicacion): #^->inicia la cadena, [a-zA-Z\s]->se refiere a solo letras y espacios, +-> que un caracter coincida con el anterior,$->final de la cadena
            raise serializers.ValidationError("La ubicación solo puede contener letras y espacios.")
        
        inputcupo = ['cupo']
        # Validar que el cupo sea un entero positivo
        if inputcupo <= 0:
            raise serializers.ValidationError("El cupo debe ser un número entero positivo.")
          # Validar que el cupo no sea igual a 0 ni mayor a 5.
        if inputcupo == 0:
            raise serializers.ValidationError("El cupo no puede ser igual a cero.")
        if inputcupo > 5:
            raise serializers.ValidationError("El cupo no puede ser mayor a cinco.")
        
        return data
    

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Entrada
        fields= '__all__'

    def validate(self, data):
        inputprecio = ['precio']
        # Validar que el campo no esté vacío
        if inputprecio is None or str(inputprecio).strip() == '':
            raise serializers.ValidationError("El campo precio no puede estar vacío.")
        # Validar que el precio sea un número positivo
        try:
            inputprecio = float(inputprecio)
        except ValueError:
            raise serializers.ValidationError("El precio debe ser un número válido.")
        # Validar que no sea un número negativo
        if inputprecio < 0:
            raise serializers.ValidationError("El precio no puede ser un número negativo.")
        # Validar que no contenga caracteres especiales
        if not str(inputprecio).replace('.', '', 1).isdigit():  # Permite un solo punto decimal
            raise serializers.ValidationError("El precio no puede contener caracteres especiales.")
        # Validar que el precio no sea excesivamente alto (esto es solo un ejemplo)
        if inputprecio < 50000:
            raise serializers.ValidationError("El precio no puede ser menor a 50,000.")
        if inputprecio > 500000:
            raise serializers.ValidationError("El precio no puede ser superior a 500,000.")
       
        inputarea = ['area_designada']
        # Validar que el campo no esté vacío
        if len(inputarea.strip()) == 0:
            raise serializers.ValidationError("El área designada no puede estar vacía.")
        # Validar longitud máxima
        if len(inputarea) > 100:
            raise serializers.ValidationError("El área designada no puede tener más de 100 caracteres.")
        # Validar que no contenga números
        if any(char.isdigit() for char in inputarea):
            raise serializers.ValidationError("El área designada no puede contener números.")
        # Validar que no contenga caracteres especiales
        if not re.match(r'^[a-zA-Z\s]+$', inputarea):
            raise serializers.ValidationError("El área designada solo puede contener letras y espacios.")
       
        inputfecha_reserva = ['fecha_reserva']
        # Validar que el campo no esté vacío
        if not inputfecha_reserva:
            raise serializers.ValidationError("La fecha de reserva no puede estar vacía.")
        # Validar que la fecha no contenga caracteres especiales
        fecha_str = str(inputfecha_reserva)
        if not fecha_str.isdigit() and not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_str):  
            raise serializers.ValidationError("La fecha de reserva no puede contener caracteres especiales.")
        # Validar que la fecha de reserva no esté en el pasado
        if inputfecha_reserva < date.today():
            raise serializers.ValidationError("La fecha de reserva no puede estar en el pasado.")
        
        # Obtener la fecha del concierto desde el campo id_concierto
        concierto = ['id_concierto']
        if concierto and inputfecha_reserva > concierto.fecha:
            raise serializers.ValidationError("La fecha de reserva no puede ser posterior a la fecha del concierto.")
        

        return data

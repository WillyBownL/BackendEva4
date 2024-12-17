from datetime import date, time
import re
from rest_framework import serializers
from appCliente.models import cliente
from appConcierto.models import Concierto
from appEntrada.models import Entrada

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

    def validate(self, data):
        # Validar el teléfono
        telefono = data.get('telefono')
        if not telefono or not str(telefono).isdigit() or len(str(telefono)) != 9:
            raise serializers.ValidationError({"telefono": "El teléfono debe tener exactamente 9 dígitos numéricos."})
        
        # Validar el correo
        correo = data.get('correo')
        correo_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not correo or not re.match(correo_regex, correo):
            raise serializers.ValidationError({"correo": "Ingrese un correo electrónico válido (formato: ejemplo@dominio.com)."})

        # Validar el RUT
        rut = data.get('rut')
        rut_regex = r'^\d{7,8}-[0-9kK]$'  
        if not rut or not re.match(rut_regex, rut):
            raise serializers.ValidationError({"rut": "Ingrese un RUT válido (formato: XXXXXXXX-X)."})
        
        return data


class ConciertoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Concierto
        fields= '__all__'

    
    def validate(self, data):
        # Validar el nombre del artista
        artista = data.get('artista', '').strip()
        if not artista:
            raise serializers.ValidationError({"artista": "El nombre del artista no puede estar vacío."})
        if len(artista) > 35:
            raise serializers.ValidationError({"artista": "El nombre del artista no puede tener más de 35 caracteres."})

        # Validar la fecha del concierto
        fecha = data.get('fecha')
        if not fecha:
            raise serializers.ValidationError({"fecha": "La fecha del concierto es obligatoria."})
        if fecha < date.today():
            raise serializers.ValidationError({"fecha": "La fecha del concierto no puede estar en el pasado."})

        # Validar la hora del concierto (18:00 - 03:00)
        hora = data.get('hora')
        if not hora:
            raise serializers.ValidationError({"hora": "La hora del concierto es obligatoria."})
        if not (time(18, 0) <= hora or hora <= time(3, 0)):
            raise serializers.ValidationError({"hora": "La hora del concierto debe estar entre las 18:00 y las 03:00."})

        # Validar la ubicación del concierto
        ubicacion = data.get('ubicacion', '').strip()
        if not ubicacion:
            raise serializers.ValidationError({"ubicacion": "La ubicación no puede estar vacía."})
        if len(ubicacion) > 50:
            raise serializers.ValidationError({"ubicacion": "La ubicación no puede tener más de 50 caracteres."})
        if not re.match(r'^[a-zA-Z\s]+$', ubicacion):
            raise serializers.ValidationError({"ubicacion": "La ubicación solo puede contener letras y espacios."})

        # Validar el cupo del concierto
        cupo = data.get('cupo')
        if not isinstance(cupo, int) or cupo <= 0:
            raise serializers.ValidationError({"cupo": "El cupo debe ser un número entero positivo."})
        if cupo > 5:
            raise serializers.ValidationError({"cupo": "El cupo no puede ser mayor a cinco."})

        return data    

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Entrada
        fields= '__all__'

    def validate(self, data):
        # Validar el precio
        precio = data.get('precio')
        if precio is None:
            raise serializers.ValidationError({"precio": "El campo precio no puede estar vacío."})
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise serializers.ValidationError({"precio": "El precio debe ser un número positivo."})
        if precio < 50000:
            raise serializers.ValidationError({"precio": "El precio no puede ser menor a 50,000."})
        if precio > 500000:
            raise serializers.ValidationError({"precio": "El precio no puede ser superior a 500,000."})

        # Validar el área designada
        area_designada = data.get('area_designada', '').strip()
        if not area_designada:
            raise serializers.ValidationError({"area_designada": "El área designada no puede estar vacía."})
        if len(area_designada) > 100:
            raise serializers.ValidationError({"area_designada": "El área designada no puede tener más de 100 caracteres."})
        if any(char.isdigit() for char in area_designada):
            raise serializers.ValidationError({"area_designada": "El área designada no puede contener números."})
        if not re.match(r'^[a-zA-Z\s]+$', area_designada):
            raise serializers.ValidationError({"area_designada": "El área designada solo puede contener letras y espacios."})

        # Validar la fecha de reserva
        fecha_reserva = data.get('fecha_reserva')
        if fecha_reserva is None:
            raise serializers.ValidationError({"fecha_reserva": "La fecha de reserva no puede estar vacía."})
        if not isinstance(fecha_reserva, date):
            raise serializers.ValidationError({"fecha_reserva": "La fecha de reserva debe estar en formato YYYY-MM-DD."})
        if fecha_reserva < date.today():
            raise serializers.ValidationError({"fecha_reserva": "La fecha de reserva no puede estar en el pasado."})

        # Validar que la fecha de reserva no sea posterior a la fecha del concierto
        id_concierto = data.get('id_concierto')
        if id_concierto and isinstance(id_concierto, Concierto):
            if fecha_reserva > id_concierto.fecha:
                raise serializers.ValidationError({"fecha_reserva": "La fecha de reserva no puede ser posterior a la fecha del concierto."})

        return data


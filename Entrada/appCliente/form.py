import re
from django import forms
from appCliente.models import cliente
from django.core.validators import EmailValidator
from appApi.views import ClienteListCreateView

class FormCliente(forms.ModelForm):
    # Validar telefono, correo y RUT

    def clean_telefono(self):
        inputTelefono = self.cleaned_data.get('telefono')
        if not inputTelefono:
            raise forms.ValidationError("El teléfono no puede estar vacío.")
        if len(inputTelefono) != 9:
            raise forms.ValidationError("El teléfono debe tener un número válido (9 dígitos).")
        if not inputTelefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return inputTelefono
    
    def clean_correo(self):
        inputCorreo = self.cleaned_data.get('correo')
        correo_regex = r'^[a-zA-Z0-9._%+-]+@[a-zAyz0-9.-]+\.[a-zA-Z]{2,}$'
        if not inputCorreo:
            raise forms.ValidationError("El correo no puede estar vacío.")
        # Usar la expresión regular para validar el formato
        if not re.match(correo_regex, inputCorreo):
            raise forms.ValidationError("Ingrese un correo electrónico válido (formato: ejemplo@dominio.com)")

        # Validación adicional con el validador de Django
        validator = EmailValidator()
        try:
            validator(inputCorreo)
        except forms.ValidationError:
            raise forms.ValidationError("Ingrese un correo electrónico válido.")
        
        return inputCorreo
    
    def clean_rut(self):
        inputRut = self.cleaned_data.get('rut')
        if not inputRut:
            raise forms.ValidationError("El RUT no puede estar vacío.")
        
        # Expresión regular para validar el formato general del RUT
        rut_regex = r'^\d{7,8}-[0-9kK]$'
        if not re.match(rut_regex, inputRut):
            raise forms.ValidationError("Ingrese un RUT válido (formato: XXXXXXXX-X)")

        # Función para validar el dígito verificador del RUT
        def validar_rut(rut):
            rut = rut.replace("-", "")  # Eliminar guion
            rut_cuerpo = rut[:-1]  # Los primeros 7 u 8 dígitos
            rut_dv = rut[-1].upper()  # El dígito verificador
            suma = 0
            multiplo = 2
            for i in reversed(range(len(rut_cuerpo))):
                suma += int(rut_cuerpo[i]) * multiplo
                multiplo = 9 if multiplo == 2 else multiplo + 1
            dv_calculado = 11 - (suma % 11)
            dv_calculado = "K" if dv_calculado == 10 else "0" if dv_calculado == 11 else str(dv_calculado)
            return rut_dv == dv_calculado
        
        # Validar que el RUT ingresado sea válido
        if not validar_rut(inputRut):
            raise forms.ValidationError("El RUT ingresado no es válido.")
        
        return inputRut

    class Meta:
        model = cliente
        fields = '__all__'
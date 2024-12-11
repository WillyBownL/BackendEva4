import re
from django import forms
from appCliente.models import cliente
from appApi.views import ClienteListCreateView

class FormCliente(forms.ModelForm):
    # Validar rut correo y telefono

    def clean_telefono(self):
        inputTelefono = self.cleaned_data.get('telefono')
        if not inputTelefono or len(inputTelefono) != 9:
            raise forms.ValidationError("El telefono debe tener un número válido (9 dígitos)")
        return inputTelefono
    
    def clean_correo(self):
        inputCorreo = self.cleaned_data.get('correo')
        correo_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not inputCorreo or inputCorreo.find('@')== -1 or not re.match(correo_regex, inputCorreo):
            raise forms.ValidationError("Ingrese un correo electrónico válido (formato: ejemplo@dominio.com)")
        
        return inputCorreo
    
    def clean_rut(self):
        inputRut = self.cleaned_data.get('rut')
        rut_regex = r'^\d{7,8}-[0-9kK]$'
        if not re.match(rut_regex, inputRut) or not inputRut or len(inputRut) < 9 or len(inputRut) > 10 or inputRut.find('-')== -1:
            raise forms.ValidationError("Ingrese un RUT válido (formato: XXXXXXXX-X)")

        return inputRut
    
        

    class Meta:
        model= cliente
        fields= '__all__'

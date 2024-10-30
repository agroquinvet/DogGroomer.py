from django import forms
from .models import Cliente, Mascota

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellido', 'correo', 'telefono']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'fecha_nacimiento', 'raza', 'descripcion']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),  # Usa 'DateInput' para fechas
            
        }

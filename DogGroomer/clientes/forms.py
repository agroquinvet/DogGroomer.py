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

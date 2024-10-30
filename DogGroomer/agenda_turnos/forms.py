from django import forms
from clientes.models import Cliente
from .models import Turno

class DniForm(forms.Form):
    dni = forms.CharField(label='DNI del Cliente', max_length=10)

class TurnoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)  # Extraer cliente de kwargs
        super().__init__(*args, **kwargs)
        if cliente:
            self.fields['mascota'].queryset = cliente.mascotas.all()

    class Meta:
        model = Turno
        fields = ['mascota', 'servicio', 'fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Usa 'DateInput' para fechas
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        mascota = cleaned_data.get('mascota')
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')

        if mascota and fecha and hora:
            # Verificar si ya existe un turno con la misma mascota, fecha y hora
            turnos_existentes = Turno.objects.filter(mascota=mascota, fecha=fecha, hora=hora)
            if turnos_existentes.exists():
                raise forms.ValidationError("Ya existe un turno agendado para esta mascota en la misma fecha y hora.")
        
        return cleaned_data

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Cliente(models.Model):
    dni = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"

class Mascota(models.Model):
    RAZAS = [
        ('bulldog_frances', 'Bulldog Francés'),
        ('golden', 'Golden Retriever'),
        ('caniche', 'Caniche'),
       
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    raza = models.CharField(max_length=100, choices=RAZAS)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.raza}"

# Crear un receptor para la señal pre_delete esto sirve para eliminar las mascotas asociadas a un cliente en especifico que se desea eliminar
@receiver(pre_delete, sender=Cliente)
def eliminar_mascotas(sender, instance, **kwargs):
    instance.mascotas.all().delete()

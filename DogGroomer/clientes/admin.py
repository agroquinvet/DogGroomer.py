from django.contrib import admin
from .models import Cliente, Mascota

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    search_fields = ['dni', 'nombre', 'apellido', 'correo', 'telefono']   
    list_filter = ['nombre', 'apellido', 'correo']
    ordering = ['apellido', 'nombre']   
    list_display = ['dni', 'nombre', 'apellido', 'correo', 'telefono']

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
   
    search_fields = ['nombre', 'raza', 'cliente__nombre', 'cliente__apellido'] 
    list_filter = ['raza', 'fecha_nacimiento']   
    ordering = ['nombre', 'fecha_nacimiento']   
    list_display = ['nombre', 'raza', 'cliente', 'fecha_nacimiento']



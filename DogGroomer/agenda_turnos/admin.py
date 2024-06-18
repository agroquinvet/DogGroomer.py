from django.contrib import admin
from .models import Servicio, Turno

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):    
    search_fields = ['nombre']   
    list_display = ['nombre']
    
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):    
    search_fields = ['cliente__nombre', 'mascota__nombre', 'servicio__nombre', 'fecha', 'hora']
   
    list_filter = ['cliente', 'mascota', 'servicio', 'fecha']
   
    ordering = ['fecha', 'hora']
   
    list_display = ['cliente', 'mascota', 'servicio', 'fecha', 'hora']



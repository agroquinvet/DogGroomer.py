from django.urls import path, re_path
from .views import IngresarDniView, AgendarTurnoView, TurnoConfirmadoView, TurnosSemanaView, EliminarTurnoView, ModificarTurnoView

urlpatterns = [
    path('ingresar_dni/', IngresarDniView.as_view(), name='ingresar_dni'),
    path('agendar_turno/<int:cliente_id>/', AgendarTurnoView.as_view(), name='agendar_turno'),
    path('turno_confirmado/<int:pk>/', TurnoConfirmadoView.as_view(), name='turno_confirmado'),
    path('turnos_semana/<int:semana>/', TurnosSemanaView.as_view(), name='turnos_semana'),
    re_path(r'^turnos-semana/(?P<semana>-?\d+)/$', TurnosSemanaView.as_view(), name='turnos_semana'),
    path('eliminar_turno/<int:pk>/', EliminarTurnoView.as_view(), name='eliminar_turno'),
    path('modificar_turno/<int:pk>/', ModificarTurnoView.as_view(), name='modificar_turno'),
]

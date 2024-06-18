from django.urls import path
from .views import BuscarClienteView, DetalleClienteView, AgregarClienteView, ModificarClienteView, EliminarClienteView, AgregarMascotaView, ModificarMascotaView, EliminarMascotaView

urlpatterns = [
    path('buscar_cliente/', BuscarClienteView.as_view(), name='buscar_cliente'),
    path('detalle_cliente/<int:pk>/', DetalleClienteView.as_view(), name='detalle_cliente'),
    path('agregar_cliente/', AgregarClienteView.as_view(), name='agregar_cliente'),
    path('modificar_cliente/<int:pk>/', ModificarClienteView.as_view(), name='modificar_cliente'),
    path('eliminar_cliente/<int:pk>/', EliminarClienteView.as_view(), name='eliminar_cliente'),
    path('agregar_mascota/<int:cliente_id>/', AgregarMascotaView.as_view(), name='agregar_mascota'),
    path('modificar_mascota/<int:pk>/', ModificarMascotaView.as_view(), name='modificar_mascota'),
    path('eliminar_mascota/<int:pk>/', EliminarMascotaView.as_view(), name='eliminar_mascota'),
]

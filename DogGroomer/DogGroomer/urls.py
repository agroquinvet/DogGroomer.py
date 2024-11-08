"""
URL configuration for DogGroomer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py en el directorio del proyecto
from django.contrib import admin
from django.urls import path, include
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('clientes/', include('clientes.urls')),
    path('turnos/', include('agenda_turnos.urls')),
    path('', include('acercade.urls')),
    
]

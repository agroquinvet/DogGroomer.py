from django.urls import path

from agendadeturnos.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    
]
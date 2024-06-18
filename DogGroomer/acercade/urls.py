from django.urls import path
from .views import AcercaDeView

urlpatterns = [
    path('', AcercaDeView.as_view(), name='acercade'),
   
]

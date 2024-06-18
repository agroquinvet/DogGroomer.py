# urls.py en account
from django.urls import path
from django.urls import path
from .views import RegisterView, RegisterSuccessView, CustomLoginView, ProfileView, HomeView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='acercade'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register_success/', RegisterSuccessView.as_view(), name='register_success'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('home/', HomeView.as_view(), name='home'),
    
]

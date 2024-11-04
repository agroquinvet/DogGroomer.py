from django.urls import reverse
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import PasswordChangeView

class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = CustomUserCreationForm
    success_url = '/account/register_success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class RegisterSuccessView(TemplateView):
    template_name = 'account/register_success.html'

class CustomLoginView(LoginView):
    template_name = 'account/login.html'

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_url = '/home/' 

class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'account/profile.html'
    form_class = CustomUserChangeForm
    success_url = '/home/' 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class HomeView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        semana_actual = 0  
        return reverse('turnos_semana', args=[semana_actual])
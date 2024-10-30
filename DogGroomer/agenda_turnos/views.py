from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import timedelta
from django.views.generic import FormView, DetailView, TemplateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin  
from .models import Cliente, Turno, Mascota
from .forms import DniForm, TurnoForm

class IngresarDniView(LoginRequiredMixin, FormView):  
    template_name = 'ingresar_dni.html'
    form_class = DniForm

    def form_valid(self, form):
        dni = form.cleaned_data['dni']
        cliente = Cliente.objects.filter(dni=dni).first()
        if cliente:
            return redirect('agendar_turno', cliente_id=cliente.id)
        else:
            form.add_error('dni', 'Cliente no encontrado')
            return self.form_invalid(form)

class AgendarTurnoView(LoginRequiredMixin, FormView):
    template_name = 'agendar_turno.html'
    form_class = TurnoForm

    def dispatch(self, request, *args, **kwargs):
        self.cliente = get_object_or_404(Cliente, id=kwargs['cliente_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['cliente'] = self.cliente  # Pasar el cliente al formulario
        return kwargs

    def form_valid(self, form):
        turno = form.save(commit=False)
        turno.cliente = self.cliente
        turno.save()
        return redirect('turno_confirmado', pk=turno.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = self.cliente
        context['mascotas'] = Mascota.objects.filter(cliente=self.cliente)
        return context


class TurnoConfirmadoView(LoginRequiredMixin, DetailView):  
    model = Turno
    template_name = 'turno_confirmado.html'
    context_object_name = 'turno'

class TurnosSemanaView(LoginRequiredMixin, TemplateView): 
    template_name = 'turnos_semana.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semana = int(self.kwargs.get('semana', 0))

        hoy = timezone.now().date()
        inicio_semana = hoy - timedelta(days=hoy.weekday()) + timedelta(weeks=semana)
        fin_semana = inicio_semana + timedelta(days=6)

        turnos = Turno.objects.filter(fecha__range=[inicio_semana, fin_semana]).order_by('fecha', 'hora')

        dias = []
        for i in range(7):
            dia = inicio_semana + timedelta(days=i)
            turnos_dia = turnos.filter(fecha=dia)
            dias.append((dia, turnos_dia))

        context['dias'] = dias
        context['semana_anterior'] = semana - 1
        context['semana_siguiente'] = semana + 1
        return context

class EliminarTurnoView(LoginRequiredMixin, DeleteView):
    model = Turno
    template_name = 'eliminar_turno.html'
    success_url = reverse_lazy('home')
 

    
class ModificarTurnoView(LoginRequiredMixin, UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'modificar_turno.html'
    context_object_name = 'turno'

    def get_success_url(self):
        return reverse('turno_confirmado', kwargs={'pk': self.object.id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        cliente = self.object.cliente  
        kwargs['cliente'] = cliente  
        return kwargs


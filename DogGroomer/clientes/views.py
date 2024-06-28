from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView, DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from .models import Cliente, Mascota
from .forms import ClienteForm, MascotaForm

class BuscarClienteView(View):
    def get(self, request):
        return render(request, 'clientes/buscar_cliente.html')

    def post(self, request):
        dni = request.POST.get('dni')
        cliente = Cliente.objects.filter(dni=dni).first()
        if cliente:
            return redirect('detalle_cliente', cliente_id=cliente.id)
        else:
            form = ClienteForm(initial={'dni': dni})
            return render(request, 'clientes/agregar_cliente.html', {'form': form})

class DetalleClienteView(DetailView):
    model = Cliente
    template_name = 'clientes/detalle_cliente.html'
    context_object_name = 'cliente'

class AgregarClienteView(FormView):
    template_name = 'clientes/agregar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('buscar_cliente')

    def form_valid(self, form):
        cliente = form.save()
        return redirect('agregar_mascota', cliente_id=cliente.id)

class ModificarClienteView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/modificar_cliente.html'
    context_object_name = 'cliente'

    def get_success_url(self):
        return reverse('detalle_cliente', kwargs={'pk': self.object.id})

class EliminarClienteView(DeleteView):
    model = Cliente
    template_name = 'clientes/confirmar_eliminar_cliente.html'
    success_url = reverse_lazy('buscar_cliente')

class AgregarMascotaView(FormView):
    template_name = 'clientes/agregar_mascota.html'
    form_class = MascotaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = get_object_or_404(Cliente, pk=self.kwargs['cliente_id'])
        return context

    def form_valid(self, form):
        cliente = get_object_or_404(Cliente, pk=self.kwargs['cliente_id'])
        mascota = form.save(commit=False)
        mascota.cliente = cliente
        mascota.save()
        return redirect('detalle_cliente', pk=cliente.id)

class ModificarMascotaView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'clientes/modificar_mascota.html'
    context_object_name = 'mascota'

    def get_success_url(self):
        return reverse('detalle_cliente', kwargs={'pk': self.object.cliente.id})

class EliminarMascotaView(DeleteView):
    model = Mascota
    template_name = 'clientes/confirmar_eliminar_mascota.html'

    def get_success_url(self):
        return reverse('detalle_cliente', kwargs={'pk': self.object.cliente.id})


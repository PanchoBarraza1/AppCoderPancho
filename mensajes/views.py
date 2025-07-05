from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Mensaje
from .forms import MensajeForm

class EnviarMensajeView(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'mensajes/enviar_mensaje.html'
    success_url = reverse_lazy('bandeja')

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)

class BandejaEntradaView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'mensajes/bandeja.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        return Mensaje.objects.filter(receptor=self.request.user).order_by('-fecha')

class DetalleMensajeView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'mensajes/detalle_mensaje.html'
    context_object_name = 'mensaje'

    def get_object(self, queryset=None):
        mensaje = super().get_object(queryset)
        if mensaje.receptor == self.request.user and not mensaje.leido:
            mensaje.leido = True
            mensaje.save()
        return mensaje

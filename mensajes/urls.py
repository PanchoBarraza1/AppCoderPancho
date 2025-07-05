from django.urls import path
from .views import EnviarMensajeView, BandejaEntradaView, DetalleMensajeView

urlpatterns = [
    path('enviar/', EnviarMensajeView.as_view(), name='enviar_mensaje'),
    path('bandeja/', BandejaEntradaView.as_view(), name='bandeja'),
    path('mensaje/<int:pk>/', DetalleMensajeView.as_view(), name='detalle_mensaje'),
]

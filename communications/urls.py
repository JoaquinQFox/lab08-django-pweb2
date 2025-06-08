from django.urls import path
from .views import correo_enviado, crear_correo

urlpatterns = [
    path('', crear_correo, name='crear_correo'),
    path('enviar_correo/', correo_enviado, name='enviar_correo'),
]


from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    color_barra = models.CharField(
        max_length=20,
        choices=[
            ('primary', 'Azul'),
            ('secondary', 'Gris'),
            ('success', 'Verde'),
            ('danger', 'Rojo'),
            ('warning', 'Amarillo'),
            ('info', 'Celeste')
        ],
        default='primary'
    )
    modo_oscuro = models.BooleanField(default=False)

    def __str__(self):
        return f"Configuración de {self.user.username}"

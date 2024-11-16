from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User  # Importar el modelo de usuario de Django

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona con el usuario autenticado
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return self.titulo

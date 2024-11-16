from django.urls import path
from . import views  # Importar las vistas

urlpatterns = [
    path('agregar/', views.agregar_publicacion, name='agregar_publicacion'),  # Vista para agregar publicaciones
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),  # Vista para registrar un nuevo usuario
    path('', views.lista_publicaciones, name='lista_publicaciones'),  # Vista para listar publicaciones
]


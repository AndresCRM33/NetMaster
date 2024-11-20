from django.urls import path
from . import views  # Importar las vistas

urlpatterns = [
    path('agregar/', views.agregar_publicacion, name='agregar_publicacion'),  # Vista para agregar publicaciones
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),  # Vista para registrar un nuevo usuario
    path('', views.lista_publicaciones, name='lista_publicaciones'),  # Vista para listar publicaciones
]


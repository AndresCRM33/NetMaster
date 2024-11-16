from django.shortcuts import render, redirect
from .models import Publicacion
from django.shortcuts import render, redirect  # Importa funciones para renderizar plantillas y redirigir
from django.contrib.auth.models import User  # Modelo de usuario predeterminado de Django
from django.contrib.auth import login  # Función para iniciar sesión automáticamente después del registro
from django.contrib import messages  # Para mostrar mensajes de éxito o error al usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib.auth import logout
from .forms import PublicacionForm  # Aquí se importa el formulario

#http://127.0.0.1:8000/

def registrar_usuario(request):
    if request.method == 'POST':  # Verifica si el formulario se envió usando POST
        username = request.POST.get('username')  # Obtiene el nombre de usuario del formulario
        email = request.POST.get('email')  # Obtiene el correo electrónico del formulario
        password = request.POST.get('password')  # Obtiene la contraseña del formulario
        confirmar_password = request.POST.get('confirmar_password')  # Obtiene la confirmación de contraseña

        # Validar que las contraseñas coincidan
        if password != confirmar_password:  # Si las contraseñas no coinciden
            messages.error(request, "Las contraseñas no coinciden.")  # Envía un mensaje de error al usuario
            return redirect('registrar_usuario')  # Redirige de nuevo al formulario de registro

        # Intentar crear un nuevo usuario
        try:
            # `create_user` crea un usuario con nombre, email y contraseña en la base de datos
            usuario = User.objects.create_user(username=username, email=email, password=password)
            usuario.save()  # Guarda el usuario en la base de datos
            login(request, usuario)  # Inicia sesión automáticamente al usuario recién registrado
            messages.success(request, "Usuario registrado exitosamente.")  # Envía un mensaje de éxito
            return redirect('lista_publicaciones')  # Redirige al usuario a la lista de publicaciones
        except Exception as e:  # Captura cualquier error que ocurra durante el registro
            messages.error(request, f"Error al registrar usuario: {e}")  # Envía un mensaje de error con el detalle
            return redirect('registrar_usuario')  # Redirige al formulario de registro

    # Si el método es GET, muestra el formulario de registro
    return render(request, 'netmaster_app/registro.html')  # Renderiza la plantilla del formulario


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Iniciar sesión al usuario
            auth_login(request, form.get_user())
            next_url = request.GET.get('next', '/')  # Redirigir a la URL deseada después del login
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'netmaster_app/login.html', {'form': form})  # Ruta a tu plantilla personalizad

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página de login (asegúrate de que 'login' esté definido en urls.py)

@login_required
def agregar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            # Asigna el autor como el usuario que está actualmente autenticado
            publicacion.autor = request.user
            publicacion.save()
            messages.success(request, "¡Publicación agregada con éxito!")
            return redirect('lista_publicaciones')
        else:
            messages.error(request, "Hubo un error al agregar la publicación.")
    else:
        form = PublicacionForm()

    return render(request, 'netmaster_app/agregar_publicacion.html', {'form': form})

@login_required
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')  # Evita duplicados con .distinct() si es necesario
    return render(request, 'netmaster_app/listar_publicaciones.html', {'publicaciones': publicaciones})


# Create your views here.

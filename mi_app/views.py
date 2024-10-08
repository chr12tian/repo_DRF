from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroUsuarioForm
from .models import OpcionesMenu, Usuario
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Error al crear el usuario. Por favor, verifica los datos ingresados.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.rol == 'admin':
                return redirect('home_admin')
            else:
                return redirect('home')
    return render(request, 'login.html')

def home(request):
    menus = OpcionesMenu.objects.all()
    return render(request, 'home.html', {'menus': menus})

def home_admin(request):
    if request.method == 'POST':
        # Aquí manejas el agregar a la tabla OpcionesMenu
        pass
    return render(request, 'home_admin.html')

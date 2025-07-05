from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, PerfilUsuario, Categoria
from .forms import ProductoForm, RegistroForm, ConfiguracionForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

@login_required
def inventario_list(request):
    productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'inventario_list.html', {'productos': productos})


@login_required
def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            messages.success(request, '✅ Producto creado exitosamente.')
            return redirect('inventario_list')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})


@login_required
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Producto actualizado correctamente.')
            return redirect('inventario_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form})


@login_required
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk, usuario=request.user)
    if request.method == 'POST':
        producto.delete()
        return redirect('inventario_list')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def configuracion_usuario(request):
    # Crea el perfil si no existe
    perfil, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ConfiguracionForm(instance=perfil)

    return render(request, 'configuracion.html', {'form': form})

@login_required
def categoria_crear(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Categoría creada exitosamente.')
            return redirect('inicio')  # Puedes redirigir donde prefieras
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, '👋 Has cerrado sesión exitosamente.')
    return redirect('inicio')

def about_view(request):
    return render(request, 'about.html')
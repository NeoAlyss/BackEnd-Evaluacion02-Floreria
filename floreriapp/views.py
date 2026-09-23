from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def index(request):
    total_productos = Producto.objects.count()
    disponibles = Producto.objects.filter(disponible=True).count()
    ultimos = Producto.objects.order_by('-fecha_ingreso')[:3]
    return render(request, 'floreriapp/index.html', {
        'total_productos': total_productos,
        'disponibles': disponibles,
        'ultimos': ultimos,
    })


def listado_productos(request):
    productos = Producto.objects.all().order_by('nombre')

    secciones = []
    for clave, etiqueta in Producto.CATEGORIA_CHOICES:
        secciones.append({
            'clave': clave,
            'etiqueta': etiqueta,
            'productos': productos.filter(categoria=clave),
        })

    return render(request, 'floreriapp/listado.html', {
        'secciones': secciones,
        'total_productos': productos.count(),
    })


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'floreriapp/detalle.html', {
        'producto': producto
    })


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listado_productos')
    else:
        form = ProductoForm()

    return render(request, 'floreriapp/crear.html', {
        'form': form
    })


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listado_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'floreriapp/editar.html', {
        'form': form,
        'producto': producto
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('listado_productos')

    return render(request, 'floreriapp/eliminar.html', {
        'producto': producto
    })

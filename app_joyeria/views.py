# UIII_joyeria_0475/app_joyeria/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor, Venta

def inicio_joyeria(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA PRODUCTO
# ==========================================
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        material = request.POST.get('material')
        precio = request.POST.get('precio')
        tipo = request.POST.get('tipo')
        stock = request.POST.get('stock')
        id_proveedor = request.POST.get('id_proveedor')

        proveedor = get_object_or_404(Proveedor, pk=id_proveedor)

        producto = Producto(
            nombre=nombre,
            material=material,
            precio=precio,
            tipo=tipo,
            stock=stock,
            id_proveedor=proveedor
        )
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.material = request.POST.get('material')
        producto.precio = request.POST.get('precio')
        producto.tipo = request.POST.get('tipo')
        producto.stock = request.POST.get('stock')
        id_proveedor = request.POST.get('id_proveedor')
        producto.id_proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# ==========================================
# VISTAS PARA PROVEEDOR
# ==========================================
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        tipo_suministro = request.POST.get('tipo_suministro')

        proveedor = Proveedor(
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            tipo_suministro=tipo_suministro
        )
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.apellido = request.POST.get('apellido')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.correo = request.POST.get('correo')
        proveedor.tipo_suministro = request.POST.get('tipo_suministro')
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# Vistas para Venta (PENDIENTE)
def agregar_venta(request):
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        id_empleado = request.POST.get('id_empleado')
        fecha_venta = request.POST.get('fecha_venta')
        total = request.POST.get('total')
        metodo_pago = request.POST.get('metodo_pago')
        productos_ids = request.POST.getlist('productos') # Obtiene una lista de IDs de productos

        venta = Venta(
            id_cliente=id_cliente,
            id_empleado=id_empleado,
            fecha_venta=fecha_venta,
            total=total,
            metodo_pago=metodo_pago
        )
        venta.save()
        venta.productos.set(productos_ids) # Asigna los productos a la venta

        return redirect('ver_ventas')
    productos = Producto.objects.all() # Necesario para el formulario de selección
    return render(request, 'venta/agregar_venta.html', {'productos': productos})

def ver_ventas(request):
    ventas = Venta.objects.all().prefetch_related('productos') # Optimizamos para cargar productos
    return render(request, 'venta/ver_ventas.html', {'ventas': ventas})

def actualizar_venta(request, id_venta):
    venta = get_object_or_404(Venta, pk=id_venta)
    if request.method == 'POST':
        venta.id_cliente = request.POST.get('id_cliente')
        venta.id_empleado = request.POST.get('id_empleado')
        venta.fecha_venta = request.POST.get('fecha_venta')
        venta.total = request.POST.get('total')
        venta.metodo_pago = request.POST.get('metodo_pago')
        productos_ids = request.POST.getlist('productos')
        venta.save()
        venta.productos.set(productos_ids) # Actualiza la relación Many-to-Many

        return redirect('ver_ventas')
    productos_disponibles = Producto.objects.all()
    # Para saber qué productos están seleccionados en el formulario
    productos_seleccionados_ids = venta.productos.values_list('id_producto', flat=True)

    context = {
        'venta': venta,
        'productos_disponibles': productos_disponibles,
        'productos_seleccionados_ids': list(productos_seleccionados_ids)
    }
    return render(request, 'venta/actualizar_venta.html', context)

def borrar_venta(request, id_venta):
    venta = get_object_or_404(Venta, pk=id_venta)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})
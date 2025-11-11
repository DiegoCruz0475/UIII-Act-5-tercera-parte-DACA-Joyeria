# UIII_joyeria_0475/app_joyeria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_joyeria, name='inicio_joyeria'),

    # URLs para Productos
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.ver_productos, name='ver_productos'),
    path('productos/actualizar/<int:id_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),

    # URLs para Proveedores
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedores/actualizar/<int:id_proveedor>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/borrar/<int:id_proveedor>/', views.borrar_proveedor, name='borrar_proveedor'),

    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('ventas/actualizar/<int:id_venta>/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/borrar/<int:id_venta>/', views.borrar_venta, name='borrar_venta'),
]
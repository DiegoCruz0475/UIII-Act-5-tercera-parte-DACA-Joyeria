# UIII_joyeria_0475/app_joyeria/models.py
from django.db import models

# ==========================================
# MODELO: PROVEEDOR
# ==========================================

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    tipo_suministro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: PRODUCTO
# ==========================================

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100)
    stock = models.IntegerField()
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: VENTA
# ==========================================

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    id_empleado = models.IntegerField()
    fecha_venta = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    productos = models.ManyToManyField(Producto, related_name='ventas')

    def __str__(self):
        return f"Venta #{self.id_venta} - Total: ${self.total}"
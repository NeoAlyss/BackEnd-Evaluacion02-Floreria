from django.db import models
from django.core.validators import MinValueValidator


class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('ramo', 'Ramo'),
        ('canasta', 'Canasta'),
        ('jarron', 'Jarrón'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='ramo')
    precio = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

from django.db import models

################ - PRODUCTOS - ################
#Tabla usuario
class Usuario(models.Model):
    usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=8)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=10)

    def __str__(self):
        return self.usuario
    
#Tabla Productos
class Producto(models.Model):
    cod_producto = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=40)
    descripcion = models.CharField(max_length=100)
    referencia = models.CharField(max_length=8)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.CharField(max_length=100)
    imagen= models.ImageField(upload_to='image/',)
    #llave foranea
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre







from django.db import models

# Create your models here.
class Factura(models.Model):
    numFactura=models.CharField(max_length=16)
    empresa=models.CharField(max_length=30)
    fechaMax=models.DateField()
    cantidad=models.FloatField()
    estado=models.CharField(max_length=10)

    def __str__(self):
        return "{}".format(self.name)
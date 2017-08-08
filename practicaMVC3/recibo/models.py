from __future__ import unicode_literals

from django.db import models

class Recibo(models.Model):
    numRecibo=models.CharField(max_length=16)
    fechaPago=models.DateField()
    cantidad=models.FloatField()
    cliente=models.CharField(max_length=50)
    concepto=models.CharField(max_length=200)
    

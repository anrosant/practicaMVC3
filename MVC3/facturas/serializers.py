from rest_framework import serializers
from .models import Factura

class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = ('numFactura', 'empresa', 'fechaMax', 'cantidad','estado')
        
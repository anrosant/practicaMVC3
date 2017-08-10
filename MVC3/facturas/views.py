from rest_framework import generics
from .serializers import FacturaSerializer
from .models import Factura

class CreateView(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
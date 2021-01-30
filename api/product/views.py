from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True).order_by("created_at")
    serializer_class = ProductSerializer


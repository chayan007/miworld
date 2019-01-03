from products.models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
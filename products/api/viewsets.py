from products.models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductModelViewSet(viewsets.ModelViewSet):
    #list, create, retrieve, update, destroy
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
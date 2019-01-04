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

class ProductViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Product
        fields = ('name', 'description', 'price', 'discount', 'days')
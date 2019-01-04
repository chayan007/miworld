from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount', 'days', 'slug')

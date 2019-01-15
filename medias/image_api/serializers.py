from medias.models import Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        lookup_field = 'post'
        extra_kwargs = {
            'url': {'lookup_field': 'post'}
        }

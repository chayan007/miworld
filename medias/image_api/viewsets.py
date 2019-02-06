from rest_framework import viewsets
from .serializers import ImageSerializer, Image
from rest_framework.permissions import IsAuthenticated


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

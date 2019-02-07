from rest_framework import viewsets
from .serializers import ImageSerializer, Image
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

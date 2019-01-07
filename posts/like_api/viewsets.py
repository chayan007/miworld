from rest_framework import viewsets
from .serializers import *
from posts.models import Like

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

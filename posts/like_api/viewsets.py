from rest_framework import viewsets
from .serializers import *
from posts.models import Like
from rest_framework.permissions import IsAuthenticated


class LikeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

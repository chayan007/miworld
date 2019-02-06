from rest_framework import viewsets
from .serializers import FollowerSerializer
from followers.models import Follower
from rest_framework.permissions import IsAuthenticated


class FollowerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

from rest_framework import viewsets
from .serializers import FollowerSerializer
from followers.models import Follower

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
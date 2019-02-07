from rest_framework import viewsets
from .serializers import FollowerSerializer
from followers.models import Follower
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FollowerViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

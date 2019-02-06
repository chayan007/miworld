from rest_framework import viewsets
from .serializers import ActualPostSerializer, Actual_Post, Post
from rest_framework.permissions import IsAuthenticated


class ActualPostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Actual_Post.objects.all()
    serializer_class = ActualPostSerializer

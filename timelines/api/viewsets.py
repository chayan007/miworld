from rest_framework import viewsets
from .serializers import ActualPostSerializer, Actual_Post, Post, APostSerializer

class ActualPostViewSet(viewsets.ModelViewSet):
    queryset = Actual_Post.objects.all()
    serializer_class = ActualPostSerializer

class APostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = APostSerializer


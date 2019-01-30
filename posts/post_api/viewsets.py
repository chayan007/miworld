from rest_framework import viewsets
from .serializers import *
from posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class ActualPostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ActualPostSerializer

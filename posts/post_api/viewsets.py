from rest_framework import viewsets
from .serializers import *
from posts.models import Post
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class ActualPostViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = ActualPostSerializer


class ActualDetailPostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = ActualDetailPostSerializer

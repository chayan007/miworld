from rest_framework import viewsets
from .serializers import *
from posts.models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

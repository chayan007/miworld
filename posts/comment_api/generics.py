from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializers import CommentSerializer, Comment
from django.contrib.auth.models import User
from notifications.models import Notification
from posts.models import Post
from rest_framework.permissions import IsAuthenticated


class CommentView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, id=None):
        if id:
            post = Post.objects.get(id=id)
            comments = Comment.objects.get(post=post)
            return comments
        else:
            return Response({'error': 'No specific post is selected'})

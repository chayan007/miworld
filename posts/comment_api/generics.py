from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializers import CommentSerializer, Comment
from django.contrib.auth.models import User
from notifications.models import Notification

class CommentView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
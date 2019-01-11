from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializers import CommentSerializer, Comment
from django.contrib.auth.models import User
from notifications.models import Notification

class CommentView(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'

    def get(self, request, id= None):
        if id:
            return self.retrieve(request, id)
        else:
            return Response({'error' : 'No specific post is selected'})

    def patch(self, request, id):
        return self.partial_update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
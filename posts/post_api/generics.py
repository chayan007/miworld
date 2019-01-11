from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from .serializers import PostSerializer
from posts.models import Post
from django.contrib.auth.models import User
from notifications.models import Notification


class PostView(generics.GenericAPIView,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin
               ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        self.create(request)
        notification = Notification(user= User.objects.get(id = request.POST['user']), notification= 'added a post')
        notification.save()
        return Response({'status' : 'true'})

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

    def patch(self, request, id):
        return self.partial_update(request, id)
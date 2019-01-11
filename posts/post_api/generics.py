from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from posts.post_api.serializers import PostSerializer
from posts.models import Post
from django.contrib.auth.models import User
from notifications.models import Notification


class PostView(generics.GenericAPIView,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.CreateModelMixin,
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
        notification = Notification(user= User.objects.get(id = request.POST['user']), notification= 'added a post', link= '')
        notification.save()
        return Response({'status' : 'true'})
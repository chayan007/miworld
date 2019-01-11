from rest_framework import generics
from rest_framework import mixins
from posts.post_api.serializers import PostSerializer
from posts.models import Post


class PostView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def __get__(self, instance, owner):
        return self.list(request)


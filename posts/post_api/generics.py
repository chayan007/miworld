from rest_framework import generics
from rest_framework import mixins
from posts.post_api.serializers import PostSerializer
from posts.models import Post


class PostView(generics.GenericAPIView, mixins.ListModelMixin,
                                        mixins.RetrieveModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)


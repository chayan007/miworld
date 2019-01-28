from rest_framework import views, mixins, generics
from rest_framework.response import Response
from medias.models import Image
from medias.image_api.serializers import ImageSerializer
from .serializers import PostSerializer, Post
from posts.models import Like, Comment

class ActualPost(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin):

    def get(self, request, id=None):
        limit = Post.objects.all().count()
        response_json = {}
        for i in range(1, limit):
            post = Post.objects.get(id=i)
            likes = Like.objects.get(post=post)
            comments = Comment.objects.get(post=post)
            response_json.update({
                "post": post,
                "likes": likes,
                "comments": comments
            })
        return Response(response_json, 200)



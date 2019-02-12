from rest_framework import mixins, generics
from rest_framework.response import Response
from .serializers import Post
from posts.models import Like, Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ActualPost(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

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

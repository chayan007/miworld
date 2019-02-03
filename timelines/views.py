from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from medias.models import Image
from posts.post_api.serializers import PostSerializer
from posts.comment_api.serializers import CommentSerializer
from posts.like_api.serializers import LikeSerializer
from medias.image_api.serializers import ImageSerializer
from posts.models import *

# Create your views here.


@api_view(['GET', ])
def actual_post_view(request, id=None):
    if request.method == 'GET':
        posts = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=posts)
        likes = Like.objects.filter(post=posts)
        images = Image.objects.filter(post=posts)
        post_serializer = PostSerializer(posts)
        like_serializer = LikeSerializer(likes, many=True)
        comment_serializer = CommentSerializer(comments, many=True)
        image_serializer = ImageSerializer(images, many=True)
        response_json = {
            "post": post_serializer.data,
            "liker": like_serializer.data,
            "comments": comment_serializer.data,
            "images": image_serializer.data
        }

        return JsonResponse(response_json, safe=False)

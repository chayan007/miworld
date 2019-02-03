from rest_framework import serializers
from timelines.models import Actual_Post, Post
from posts.post_api.serializers import PostSerializer
from posts.models import Like,Comment
from medias.image_api.serializers import ImageSerializer
from posts.like_api.serializers import LikeSerializer
from posts.comment_api.serializers import CommentSerializer


class ActualPostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)
    image = ImageSerializer(many=True)

    class Meta:
        model = Actual_Post
        fields = '__all__'

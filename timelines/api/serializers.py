from rest_framework import serializers
from timelines.models import Actual_Post
from posts.like_api.serializers import LikeSerializer
from posts.comment_api.serializers import CommentSerializer


class ActualPostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer
    comments = CommentSerializer

    class Meta:
        model = Actual_Post
        fields = '__all__'

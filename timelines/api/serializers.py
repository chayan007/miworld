from rest_framework import serializers
from timelines.models import Actual_Post, Post
from posts.post_api.serializers import PostSerializer
from posts.models import Like,Comment
from posts.like_api.serializers import LikeSerializer
from posts.comment_api.serializers import CommentSerializer


class ActualPostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Actual_Post
        fields = '__all__'

class APostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, object):
        return Like.objects.get(post=object)
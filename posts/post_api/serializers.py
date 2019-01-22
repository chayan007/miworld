from rest_framework import serializers
from posts.models import Post, Like, Comment
from medias.image_api.serializers import ImageSerializer
from django.utils.timezone import now

class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer

    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

# class ActualPostSerializer(serializers.ModelSerializer):
#     likes = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#     def get_likes(self, object):
#         return Like.objects.filter(post=object).count()

class ActualPostSerializer(serializers.ModelSerializer):
    #posts = serializers.SerializerMethodField(method_name=get_post)
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        like = Like.objects.filter(post=obj).count()
        print(like)
        return like

    def get_comments(self, obj):
        comment = Comment.objects.filter(post=obj).count()
        print(comment)
        return comment

    def get_duration(self, obj):
        if obj.created_at:
            duration = (now() - obj.created_at).days
            return duration
        else:
            return "Undefined"

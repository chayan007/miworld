from rest_framework import serializers
from django.http import HttpResponse
from datetime import datetime
from posts.models import Post, Like, Comment
from medias.models import Image
from medias.image_api.serializers import ImageSerializer
from django.core import serializers as core_serializer


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer

    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ActualPostSerializer(serializers.ModelSerializer):
    #posts = serializers.SerializerMethodField(method_name=get_post)
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField(read_only=True, )

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
            duration = (datetime.now().date() - obj.created_at).days
            return duration
        else:
            return "Undefined"

    def get_images(self, obj):
        image = Image.objects.filter(post=obj).first()
        if image != None:
            image = Image.objects.get(post=obj)
            image_serializer = core_serializer.serialize('json', [image, ])
            return image_serializer
        else:
            return "Undefined"


class ActualDetailPostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    liker = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        like = Like.objects.filter(post=obj).count()
        print(like)
        return like

    def get_liker(self, obj):
        liker = Like.objects.get(post=obj)
        print(liker)
        return liker

    def get_comments(self, obj):
        comment = Comment.objects.get(post=obj)
        print(comment)
        return comment

    def get_comments_count(self, obj):
        comment = Comment.objects.filter(post=obj).count()
        print(comment)
        return comment

    def get_images(self, obj):
        image = Image.objects.filter(post=obj).first()
        if image != None:
            image = Image.objects.get(post=obj)
            image_serializer = core_serializer.serialize('json', [image, ])
            return image_serializer
        else:
            return "Undefined"

    def get_duration(self, obj):
        if obj.created_at:
            duration = (datetime.now().date() - obj.created_at).days
            return duration
        else:
            return "Undefined"

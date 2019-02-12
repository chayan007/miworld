from rest_framework import serializers
from videos.models import Video
from users.api.serializers import UserSerializer


class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Video
        fields = '__all__'
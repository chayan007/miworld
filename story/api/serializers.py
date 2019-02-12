from rest_framework import serializers
from users.api.serializers import UserSerializer
from story.models import Story


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Story
        fields = '__all__'

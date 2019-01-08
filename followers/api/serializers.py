from rest_framework import serializers
from followers.models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'

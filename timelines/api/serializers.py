from rest_framework import serializers
from timelines.models import Actual_Post


class ActualPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actual_Post
        fields = '__all__'

from rest_framework import viewsets
from .serializers import Story, StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
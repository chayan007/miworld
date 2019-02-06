from rest_framework import viewsets
from .serializers import VideoSerializer, Video
from rest_framework.permissions import IsAuthenticated



class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
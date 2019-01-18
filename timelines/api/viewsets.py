from rest_framework import viewsets
from .serializers import ActualPostSerializer, Actual_Post

class ActualPostViewSet(viewsets.ModelViewSet):
    queryset = Actual_Post.objects.all()
    serializer_class = ActualPostSerializer
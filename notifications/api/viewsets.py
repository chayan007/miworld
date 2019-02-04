from .serializers import NotificationSerializer
from notifications.models import Notification
from rest_framework import viewsets


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
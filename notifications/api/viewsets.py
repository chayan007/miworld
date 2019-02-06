from .serializers import NotificationSerializer
from notifications.models import Notification
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

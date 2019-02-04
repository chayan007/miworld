from .serializers import NotificationSerializer
from notifications.models import Notification
from rest_framework.decorators import api_view


@api_view(['GET',])
def get_all_notifications():
    notifict = 0
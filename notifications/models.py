from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    notification = models.CharField(max_length=50)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.user.username + ' ' + self.notification

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Follower(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name='following_user')
    follower = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name='follower_user')

    def __str__(self):
        return self.follower.username + ' is following ' + self.user.username

    class Meta:
        unique_together = ('user', 'follower',)
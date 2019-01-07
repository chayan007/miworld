from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Follower(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.follower.username + ' is following ' + self.user.username
from django.db import models
import os, random, string
from django.contrib.auth.models import User

# Create your models here.


def random_name():
    name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return name


class Video(models.Model):
    title = models.TextField(default=random_name)
    description = models.TextField(null=True)
    video = models.FileField(upload_to='videos/')
    snap1 = models.ImageField(upload_to='video_snaps/', null=True)
    snap2 = models.ImageField(upload_to='video_snaps/', null=True)
    snap3 = models.ImageField(upload_to='video_snaps/', null=True)
    cover = models.ImageField(upload_to='video_snaps/', null=True)
    views = models.IntegerField(default=0)
    category = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def size(self):
        return self.video.size

    def extension(self):
        name, extension = os.path.splitext(self.video.name)
        return extension

    def name(self):
        return os.path.basename(self.video.name)

    def __str__(self):
        return self.video.name

from django.db import models
from posts.models import Post
import os

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.image.name

    def extension(self):
        name, extension = os.path.splitext(self.image.name)
        return extension

    def name(self):
        return os.path.basename(self.image.name)

    def size(self):
        return self.image.size

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    snap1 = models.ImageField(upload_to='video_snaps/', null= True)
    snap2 = models.ImageField(upload_to='video_snaps/', null= True)
    snap3 = models.ImageField(upload_to='video_snaps/', null= True)
    cover = models.ImageField(upload_to='video_snaps/', null= True)
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE, null=True)

    def size(self):
        return self.video.size

    def extension(self):
        name, extension = os.path.splitext(self.video.name)
        return extension

    def name(self):
        return os.path.basename(self.video.name)


    def __str__(self):
        return self.video.name

class Audio(models.Model):
    name = models.CharField(max_length=30 ,blank= True)
    audio = models.FileField()
    extension = models.CharField(max_length=5 ,blank= True)
    memory = models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models
from posts.models import Post

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    extension = models.CharField(max_length=5)
    memory = models.IntegerField()
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=30)
    video = models.FileField()
    snap1 = models.ImageField(upload_to='video_snaps/')
    snap2 = models.ImageField(upload_to='video_snaps/')
    snap3 = models.ImageField(upload_to='video_snaps/')
    cover = models.ImageField(upload_to='video_snaps/')
    extension = models.CharField(max_length=5)
    memory = models.IntegerField()
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

class Audio(models.Model):
    name = models.CharField(max_length=30)
    audio = models.FileField()
    extension = models.CharField(max_length=5)
    memory = models.IntegerField()

    def __str__(self):
        return self.name

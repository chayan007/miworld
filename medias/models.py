from django.db import models
from posts.models import Post
import os


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name

    def extension(self):
        name, extension = os.path.splitext(self.image.name)
        return extension

    def name(self):
        return os.path.basename(self.image.name)

    def size(self):
        return self.image.size


class Audio(models.Model):
    name = models.CharField(max_length=30 ,blank= True)
    audio = models.FileField()
    extension = models.CharField(max_length=5 ,blank= True)
    memory = models.IntegerField()

    def __str__(self):
        return self.name

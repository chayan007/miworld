from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    extension = models.CharField(max_length=5)
    memory = models.IntegerField()

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField()
    extension = models.CharField(max_length=5)
    memory = models.IntegerField()

    def __str__(self):
        return self.name

class Audio(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField()
    extension = models.CharField(max_length=5)
    memory = models.IntegerField()

    def __str__(self):
        return self.name

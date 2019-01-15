from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import random

# Create your models here.

class Post(models.Model):
    description = models.TextField(null= True, blank= True)
    views = models.IntegerField(null= True, default=0)
    slug = models.SlugField(null= True, unique= True)
    task = models.CharField(max_length=200) #updated, uploaded, shared,etc..
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        randomNum = int(random.random()*10000000000)
        hapazat = self.user.username + ' ' + str(randomNum)
        slug = slugify(hapazat)
        if self.slug != slug:
            self.slug = slug
        return super(Post, self).save()

    def __str__(self):
        return self.user.username + ' posted ' + self.slug

class Like(models.Model):
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add= True)

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return self.user.username + 'has like the post' + self.post.slug

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    hook = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.username + ' commented: ' + self.comment[:20]


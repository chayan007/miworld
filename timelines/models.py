from django.db import models
from posts.models import Post, Like, Comment
from medias.models import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Actual_Post(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE, null=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post.description[:20]

    def get_images(self):
        images = Image.objects.get(post=self.post)
        return images


def create_acutal_post(sender, instance, created, **kwargs):
    if created:
        Actual_Post.objects.get_or_create(post=instance)


def add_likes(sender, **kwargs):
    actual_post = Actual_Post.objects.get(post=kwargs['post'])
    actual_post.likes = kwargs['instance']


def add_comments(sender, instance, **kwargs):
    actual_post = Actual_Post.objects.get(post=instance.post)
    actual_post.comments = kwargs['instance']


post_save.connect(create_acutal_post, sender=Post)

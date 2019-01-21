from django.db import models
from posts.models import Post, Like, Comment
from medias.models import Image, Video
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Actual_Post(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
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

post_save.connect(create_acutal_post, sender=Post)

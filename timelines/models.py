from django.db import models
from posts.models import Post
from medias.models import Image, Video

# Create your models here.

class Actual_Post(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post.description[:20]

    def get_images(self):
        images = Image.objects.get(post=self.post)
        return images

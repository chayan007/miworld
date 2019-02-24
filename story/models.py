from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    story_text = models.TextField(max_length=300, null=True)
    story_image = models.ImageField(upload_to='story/images/', null=True)
    story_video = models.FileField(upload_to='story/videos/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

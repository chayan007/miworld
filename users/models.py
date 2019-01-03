from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=
        (('M', 'Male'),
         ('F', 'Female'),
         ('O', 'Others'),
        ))
    slug = models.SlugField(unique=True, max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    is_celeb = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    verification_id = models.FileField()

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Personal(models.Model):
    display = models.ImageField(upload_to='images/users/', null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from medias.models import Image
from django.utils.text import slugify
import random

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, to_field='id', on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=
        (('M', 'Male'),
         ('F', 'Female'),
         ('O', 'Others'),
        ))
    slug = models.SlugField(unique=True, max_length=50, null=True)
    birth_date = models.DateField(null=True, blank=True)
    is_celeb = models.BooleanField(null=True)
    is_premium = models.BooleanField(null=True)
    verification_id = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        hapazat = self.user.username
        slug = slugify(hapazat)
        if self.slug != slug:
            self.slug = slug
        return super(Profile, self).save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, slug=sender.username)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Personal(models.Model):
    display = models.ForeignKey(Image, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
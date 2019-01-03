from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.text import slugify

# Create your models here.

class User(AbstractUser):
    gender = models.CharField(choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ))
    slug = models.SlugField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    is_celeb = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    verification_id = models.FileField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + str(self.birth_date))
        super(User, self).save(*args, **kwargs)
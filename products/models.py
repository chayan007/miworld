from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    description = models.TextField()
    days = models.IntegerField()

    def __str__(self):
        return self.name


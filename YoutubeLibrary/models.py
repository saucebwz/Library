from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)

class VideoModel(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=1500)
    thumb_url = models.URLField(max_length=120)
    link = models.URLField(max_length=120)
    added_data = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='category')



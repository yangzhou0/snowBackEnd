from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Resort(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    likes = models.PositiveIntegerField(default = 0)
    latitude = models.FloatField()
    longitude = models.FloatField()
    website = models.CharField(max_length=200)
        
class Comment(models.Model):
    body = models.CharField(max_length=5000)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE,related_name='comments')
    likes = models.PositiveIntegerField(default = 0)
    author = models.CharField(max_length=100)

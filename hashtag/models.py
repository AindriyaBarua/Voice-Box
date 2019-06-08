from django.db import models
from django.conf import settings
#from post.models import Post

# Create your models here.
class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    hid = models.IntegerField()

    def __str__(self):
        return self.name

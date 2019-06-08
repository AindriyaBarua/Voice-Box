from django.db import models
from django.conf import settings
from django.utils import timezone
from hashtag.models import Hashtag

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    hid = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

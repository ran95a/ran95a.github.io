from django.db import models

from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete='None')
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    img = models.ImageField(upload_to='post_img/', default='post_img/images.jpg')
    created = models.DateTimeField(default=timezone.now)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class MyObject(models.Model):
        image_url = models.CharField

def image_url(self):
    if Post.path.exists(self.image_url):
        return self.image_url
        return 'default_image'



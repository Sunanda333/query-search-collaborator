from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    resolved = models.BooleanField(default=False)
    tags = models.CharField(max_length=1000, default='Untagged')
    doc_link = models.URLField(max_length = 200, default = 'https://docs.google.com/document/d/1PYSkN38yVxokq8gk4exA5fiT-cmCdASpP5_weZ9ThLs/edit')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Tag(models.Model):
    name = models.CharField(max_length=50)
  
    def __str__(self):
        return f"{self.name}"

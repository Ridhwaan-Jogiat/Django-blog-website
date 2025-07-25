from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def get_absolute_url(self):
    return reverse("post_detail", args={str(self.id)})


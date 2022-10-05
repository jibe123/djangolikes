from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
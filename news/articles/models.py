from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
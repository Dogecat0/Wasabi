from multiprocessing import context

from django.db import models

# Create your models here.


class Scraped(models.Model):
    link = models.URLField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

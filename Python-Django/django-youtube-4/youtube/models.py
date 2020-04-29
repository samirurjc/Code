from django.db import models

class Video(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    selected = models.BooleanField(default=False)

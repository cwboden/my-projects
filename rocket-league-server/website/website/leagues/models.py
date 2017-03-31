from django.contrib.auth.models import Permission, User
from django.db import models


class League(models.Model):
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.FileField()

    def __str__(self):
        return self.title

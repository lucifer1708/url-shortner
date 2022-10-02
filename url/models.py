from django.db import models

# Create your models here.


class Url(models.Model):
    link = models.CharField(max_length=10000000)
    alias = models.CharField(max_length=100, unique=True)

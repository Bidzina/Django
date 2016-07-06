from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    slug = models.SlugField(max_length=250,unique=True)
    title = models.CharField(max_length=250)

    def __str__(self):  #
        return self.title
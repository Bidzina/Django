from __future__ import unicode_literals

from django.db import models
from tags.models import Tag


# Create your models here.
class Subject(models.Model):
    slug = models.CharField(max_length=250,unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):  #
        return self.title

    class Meta:
        ordering = ('title',)

class Post(models.Model):
    slug = models.CharField(max_length=250, unique=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, unique=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):  #
        return self.title

    class Meta:
        ordering = ('-date',)


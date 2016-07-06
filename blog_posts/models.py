from __future__ import unicode_literals

from django.db import models
from tags.models import Tag
from django.core.urlresolvers import reverse


# Create your models here.
class Subject(models.Model):
    slug = models.SlugField(max_length=250,unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):  #
        return self.title

    def get_absolute_url(self):
        return reverse('single_subject', args=[self.slug])

    class Meta:
        ordering = ('title',)

class Post(models.Model):
    slug = models.SlugField(max_length=250, unique=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, unique=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):  #
        return self.title

    def get_absolute_url(self):
        return reverse('single_post', args=[str(self.date.year), str(self.date.month), self.slug])

    class Meta:
        ordering = ('-date',)


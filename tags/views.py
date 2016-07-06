from django.http import HttpResponse
from django.shortcuts import render
from .models import Tag

def tags(request):
    tags = Tag.objects.all()
    obj = {
        'tags': tags
    }
    return render(request, 'tags/tag_list.html', obj)

def single_tag(request, slug):
    single_tag = Tag.objects.get(slug=slug)
    obj = {
        'single_tag' : single_tag
    }
    return render(request, 'tags/tag.html', obj)
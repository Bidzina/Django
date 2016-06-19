from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Subject

def index(request):
    posts = Post.objects.all()
    subjects = Subject.objects.all()
    obj = {
        'posts': posts,
        'subjects': subjects
    }
    return render(request, 'blog_posts/blog_list.html', obj)
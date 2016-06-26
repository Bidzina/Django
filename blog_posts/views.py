from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Subject

def posts(request):
    posts = Post.objects.all()
    obj = {
        'posts': posts
    }
    return render(request, 'blog_posts/blog_list.html', obj)

def subjects(request):
    subjects = Subject.objects.all()
    obj = {
        'subjects': subjects
    }
    return render(request, 'blog_posts/subject.html', obj)
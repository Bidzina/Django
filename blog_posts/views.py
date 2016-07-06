from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Subject

def posts(request):
    posts = Post.objects.all()
    obj = {
        'posts': posts
    }
    return render(request, 'blog_posts/blog_list.html', obj)

def single_post(request, year, month, slug):
    single_post = Post.objects.get(date__year=year, date__month=month, slug=slug)
    obj = {
        'single_post': single_post
    }
    return render(request, 'blog_posts/blog.html', obj);

def subjects(request):
    subjects = Subject.objects.all()
    obj = {
        'subjects': subjects
    }
    return render(request, 'blog_posts/subject_list.html', obj)

def single_subject(request,slug):
    single_subject = Subject.objects.get(slug=slug)
    obj = {
        'single_subject': single_subject
    }
    return render(request, 'blog_posts/subject.html', obj)
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/', views.posts, name='posts'),
    url(r'^subjects/', views.subjects, name='subjects'),

]
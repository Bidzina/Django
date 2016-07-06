from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/$', views.posts, name='posts'),
    url(r'^post/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<slug>\w+)/$', views.single_post, name='single_post'),
    url(r'^subject/$', views.subjects, name='subjects'),
    url(r'^subject/(?P<slug>\w+)/$', views.single_subject, name='single_subject')
]
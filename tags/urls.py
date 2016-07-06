from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tag/$', views.tags, name='tags'),
    url(r'^tag/(?P<slug>\w+)/$', views.single_tag, name='single_tag')

]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tags/', views.tags, name='tags')

]
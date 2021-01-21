from os import name, startfile
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name='index'),
    path('engagement', views.engagement, name='engagement')
]
urlpatterns += staticfiles_urlpatterns()

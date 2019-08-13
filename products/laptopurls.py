from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'laptops'
urlpatterns = [
    path('', views.laptops, name='laptop'),
    re_path('(?P<laptop_id>[0-9]{5})', views.lap_detail, name='lap_detail'),
]

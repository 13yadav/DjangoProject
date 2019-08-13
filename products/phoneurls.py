from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'phones'
urlpatterns = [
    path('', views.phones, name='phone'),
    re_path('(?P<phone_id>[0-9]{5})', views.ph_detail, name='ph_detail'),
]

from django.http import HttpResponse, request
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path("hello_world", views.hello_world),
    path("orden", views.ordenada),
]

from django.http import HttpResponse, request
from django.contrib import admin
from django.urls import path

def hello_world(request):
    return HttpResponse("Hello, Worl!")    
urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld", hello_world),
]

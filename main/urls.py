from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='nano-home'),
    path('upload', views.upload, name='nano-upload'),
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoContent

def home(request):
    return render(request, 'main/home.html')

def upload(request):
    if request.method == 'POST':
        vc = VideoContent()
        vc.media = request.FILES["media"]
        vc.save()
    return render(request, 'main/upload.html')
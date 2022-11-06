from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import VideoContent

def home(request):
    ctx = {
        'videos': VideoContent.objects.all().order_by('-datetime'),
    }
    return render(request, 'main/home.html', ctx)

def upload(request):
    if request.method == 'POST':
        vc = VideoContent()
        vc.media = request.FILES["media"]
        vc.save()
        return HttpResponseRedirect(reverse('nano-home'))
    return render(request, 'main/upload.html')
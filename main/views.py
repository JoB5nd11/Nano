from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import VideoContent

@login_required
def home(request):
    ctx = {
        'videos': VideoContent.objects.all().order_by('-datetime'),
    }
    return render(request, 'main/home.html', ctx)

@login_required
def upload(request):
    if request.method == 'POST':
        vc = VideoContent()
        vc.media = request.FILES["media"]
        vc.save()
        return HttpResponseRedirect(reverse_lazy('nano-home'))
    return render(request, 'main/upload.html')
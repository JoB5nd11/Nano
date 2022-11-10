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

@login_required
def subscriptions(request):
    return render(request, 'main/subscriptions.html')

@login_required
def history(request):
    return render(request, 'main/history.html')

@login_required
def liked_content(request):
    return render(request, 'main/liked_content.html')

@login_required
def saved_content(request):
    return render(request, 'main/saved_content.html')

@login_required
def devlog(request):
    return render(request, 'main/devlog.html')

@login_required
def settings(request):
    return render(request, 'main/settings.html')

@login_required
def help_page(request):
    return render(request, 'main/help_page.html')

@login_required
def imprint(request):
    return render(request, 'main/imprint.html')
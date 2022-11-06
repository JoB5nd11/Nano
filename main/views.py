from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    ctx = {
        
    }
    return render(request, 'main/home.html', ctx)
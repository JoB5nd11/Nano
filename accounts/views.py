from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile

def my_login(request):
    if request.method == 'POST':
        found_users = Profile.objects.filter(username=request.POST.get('username'))
        if len(found_users) == 0:
            return HttpResponse('<h3>No User Found</h3>')

        if found_users[0].password != request.POST.get('password'):
            return HttpResponse('<h3>Wrong Password</h3>')
        
        login(request, found_users[0])
        return HttpResponseRedirect(reverse_lazy('nano-home'))

    return render(request, 'accounts/login.html')


def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('accounts-login'))


def register(request):
    if request.method == 'POST':
        if len(Profile.objects.filter(username=request.POST.get('username'))) > 0:
            return HttpResponse('<h3>This Username is already taken</h3>')

        new_profile = Profile(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
            email = request.POST.get('email'),
        )
        new_profile.save()

        return HttpResponseRedirect(reverse_lazy('accounts-login'))

    return render(request, 'accounts/register.html')

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='nano-home'),
    path('upload', views.upload, name='nano-upload'),
    path('subscriptions', views.subscriptions, name='nano-subscriptions'),
    path('history', views.history, name='nano-history'),
    path('liked', views.liked_content, name='nano-liked'),
    path('saved', views.saved_content, name='nano-saved'),
    path('devlog', views.devlog, name='nano-devlog'),
    path('settings', views.settings, name='nano-settings'),
    path('help', views.help_page, name='nano-help'),
    path('imprint', views.imprint, name='nano-imprint'),
]
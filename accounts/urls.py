from django.urls import path
from . import views 

urlpatterns = [
    path('login', views.my_login, name='accounts-login'),
    path('logout', views.my_logout, name='accounts-logout'),
    path('register', views.register, name='accounts-register'),
    #password change
    #deleteacc
]
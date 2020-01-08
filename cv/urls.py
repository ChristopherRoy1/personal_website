from django.conf.urls import url
from django.urls import path, include
from . import views
#from django.contrib.auth.views import login

urlpatterns = [
    path('', views.home)
    #path('login/', login, {'template_name': 'cv/login.html'})
]

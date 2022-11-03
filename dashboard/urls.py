from django.urls import path
from .import views


urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),
]

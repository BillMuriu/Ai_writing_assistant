from django.urls import path
from .import views


urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),

    ##Blog generation Routes
    path('generate-blog-topic', views.blogTopic, name='blog-topic'),
]

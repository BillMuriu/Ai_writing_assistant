from django.urls import path
from .import views

# const textare = btn.getAttribute('data-hex');


urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),

    ##Blog generation Routes
    path('blog-topic', views.blogTopic, name='blog-topic'),
    path('blog-sections', views.blogSectionsTitles, name='blog-sections'),

    path('billing', views.billing, name='billing'),
]

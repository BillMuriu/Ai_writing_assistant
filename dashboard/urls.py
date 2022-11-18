from django.urls import path
from .import views

# const textare = btn.getAttribute('data-hex');


urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),

    ##Blog generation Routes
    path('blog-topic', views.blogTopic, name='blog-topic'),
    path('blog-sections', views.blogSections, name='blog-sections'),

    ##Saving the blog topic for future use

    # path('save-blog-topic/<str:blogTopic>/', views.saveBlogTopic, name='save-blog-topic'),
]

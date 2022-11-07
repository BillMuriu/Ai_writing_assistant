from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

##Local Imports
from .forms import *
from .models import *
from .functions import *


@login_required
def home(request):

    context = {}

    return render(request, 'dashboard/home.html', context)


@login_required
def profile(request):
    context = {}


    if request.method == 'GET':
        form  = ProfileForm(instance=request.user.profile, user=request.user)
        context['form'] = form
        return render(request, 'dashboard/profile.html', context)

    if request.method == 'POST':
        form  =  ProfileForm(request.POST, instance=request.user.profile, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')



    return render(request, 'dashboard/profile.html', context)


def blogTopic(request):
    # context = {}

    if request.method == 'POST':
        blogIdea = request.POST['blogIdea']
        keywords = request.POST['keywords']

        blogTopics = generateBlogTopicIdeas(blogIdea, keywords)
        if len(blogTopics) > 0:
            request.session['blogTopics'] = blogTopics
            return redirect('blog-topic')
        else:
            messages.error(request,"Oops")
            return redirect('blog-topic')

    context = {}
    context['blogTopics'] = request.session['blogTopics']

    return render(request, 'dashboard/blog-topic.html', context)

# def blogTopicsGenerated(request):
#     if 'blogTopics' in request.session:
#         pass
#     else:
#         messages.error(request,"Start by creating blog topic ideas")
#         return redirect('blog-topic')
#
#     context = {}
#     context['blogTopics'] = request.session['blogTopics']
#
#     return render(request, 'dashboard/blog-topics-generated.html', context)

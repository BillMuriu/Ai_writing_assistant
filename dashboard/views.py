from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.views.decorators.http import require_POST
from django.views.decorators.http import csrf_exempt

##Local Imports
from .forms import *
from .models import *
from .functions import *


@login_required
def home(request):

    allowance = checkCountAllowance(request.user.profile)
    context = {}
    context['monthCount'] = request.user.profile.monthlyCount
    context['allowance'] = allowance

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
    context = {}

    if request.method == 'POST':
        blogIdea = request.POST['blogIdea']
        keywords = request.POST['keywords']


        blogTopics = generateBlogTopicIdeas(blogIdea, keywords, request.user.profile)
        context['blogTopics'] = blogTopics


    return render(request, 'dashboard/blog-topic.html', context)

def blogSectionsTitles(request):
    context = {}

    if request.method == 'POST':
        blogTopicIdea = request.POST['blogTopicIdea']
        keywords = request.POST['keywords']


        blogSectionTitles = generateBlogSectionTitles(blogTopicIdea, keywords, request.user.profile)
        context['blogSectionTitles'] = blogSectionTitles


    return render(request, 'dashboard/blog-sections.html', context)


def billing(request):
        context = {}
        return render(request, 'dashboard/billing.html', context)



@require_POST
@csrf_exempt
def webhook(request):
    #Verify that the request is coming from paypal
    return redirect('billing')

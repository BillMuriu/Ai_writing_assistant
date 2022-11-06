from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

##Local Imports
from .forms import *
from .models import *


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

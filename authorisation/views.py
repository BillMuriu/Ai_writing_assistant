from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ','').lower()
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials or User does not Exist")
            return redirect('register')


    return render(request, 'authorisation/login.html', {})

def register (request):

    if request.method == 'POST':
        email = request.POST['email'].replace(' ','').lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not password1 == password2:
            messages.error(request,"Passwords do not match")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request,"User already exists")
            return redirect('register')

        user = User.objects.create_user(email=email, username=email, password=password2)
        user.save()

        auth.login(request,user)
        return redirect('home')


    return render(request, 'authorisation/register.html', {})

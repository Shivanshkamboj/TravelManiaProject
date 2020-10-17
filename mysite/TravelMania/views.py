from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return HttpResponse("<h1>HOME PAGE!!!</h1>")
def about(request):
    return HttpResponse("<h1>ABOUT PAGE!!!</h1>")

#login page

def login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username1, password=password1)

        if user is None:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('login')
        else:
            return redirect('home')

    else:
        return render(request, 'TravelMania/login.html')


#register page

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Taken!')
            return redirect('/')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            messages.success(request, 'Your Account Has Been Successfully Created!')
            return redirect('/')
    else:
        return render(request, 'TravelMania/register.html')

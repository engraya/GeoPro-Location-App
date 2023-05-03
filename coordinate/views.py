from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home(request):
    return render(request, 'coordinate/home.html')


def geo_api(request):
    my_ip = requests.get('https://api.ipify.org?format=json')
    my_ip_data = json.loads(my_ip.text)
    ip_context_convert = requests.get('http://ip-api.com/json/' + "Your IP Adress" )
    geo_data = ip_context_convert.text
    geo_data_load = json.loads(geo_data)
    context = {'data' : geo_data_load}
    return render(request, 'coordinate/geo_api.html', context)



def registerUser(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful....")
            return redirect("/")
        messages.error(request, "Registration not Successful, Invalid Informtion provided, Try again Later Please!.....")
    form = CustomUserForm()
    context = {'registerForm' : form}
    return render(request, 'coordinate/registerUser.html', context)


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now Logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()

    context = {'loginForm' : form}

    return render(request, 'coordinate/loginUser.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, "You have Successfully Logged out from your account.")

    return redirect("/")



def profile(request):
    context = {}
    return render(request, 'coordinate/profile.html', context)


def landingPage(request):
    return render(request, 'coordinate/landingPage.html')

 

def infoPage(request):
    return render(request, 'coordinate/infoPage.html')
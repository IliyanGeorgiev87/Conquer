from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def HomeView(request):
    return render(request, "home.html")

def RegisterView(request):
    return render(request, 'register.html', {})

@login_required
def ListView(request):
    return render(request, 'list.html', {})

def LoginView(request):
    return render(request, 'login.html', {})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

@login_required
def ViewQuotesView(request):
    return render(request, 'quotes.html')

def HomeView(request):
    return render(request, "home.html")

def RegisterView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already exists!"})

        user = User.objects.create_user(username = username, password = password)
        UserProfile.objects.create(user = user)
        login(request, user)
        return redirect('list')

    return render(request, 'register.html', {})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('quotes')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

@login_required
def LogoutView(request):
    logout(request)
    return redirect ('home')
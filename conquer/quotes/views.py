from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import UserProfile, Quote

from django.views.generic import DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#* Account and misc:

@login_required
def ViewQuotesView(request):
    context = {
        'quotes': Quote.objects.all()
    }
    return render(request, 'quotes.html', context)

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
        return redirect('quotes')

    return render(request, 'register.html', {})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Incorrect username or password.'})
        
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

@login_required
def AccountLookupView(request):
    return render(request, 'user_account.html')


@login_required

def AccountDeleteView(request):

    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')

    return render(request, 'account_delete.html')

#* Quotes:


@login_required
def QuoteCreateView(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')

        if Quote.objects.filter(title = title).exists():
            context = {
                'error': 'Quote title already exist! Use a different one!'
            }
            return render(request, 'create.html', context)
        
        quote = Quote.objects.create(title=title, quote_text=text, quote_author = author)
        return redirect('quotes')

    return render(request, 'create.html')
    
#-
class QuoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Quote
    template_name = 'delete.html'
    success_url = reverse_lazy('quotes')
    login_url = '/login'

@login_required
def QuoteUpdateView(request,pk):
    quote = get_object_or_404(Quote,pk=pk)

    if request.method == 'POST':
        quote.title = request.POST.get('title')
        quote.quote_text = request.POST.get('text')
        quote.quote_author = request.POST.get('author')
        quote.save()

        return redirect('quotes')
    
    return render(request, 'edit.html', {'quote': quote})

class QuoteDetailVIew(LoginRequiredMixin, DetailView):
    model = Quote
    template_name = 'quote.html'
    context_object_name = 'quote'
    login_url = '/login'
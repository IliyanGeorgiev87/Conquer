from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('quotes/', views.ViewQuotesView, name='quotes'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('create/', views.CreateView, name='create')
]
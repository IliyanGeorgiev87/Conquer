from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('quotes/', views.ListView, name='quotes'),
    path('login/', views.LoginView,)
]
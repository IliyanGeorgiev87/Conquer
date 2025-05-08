from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('quotes/', views.ViewQuotesView, name='quotes'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('account/', views.AccountLookupView, name='account'),
    path('account/delete/', views.AccountDeleteView, name='account_delete'),
    #* for quotes
    path('create/', views.QuoteCreateView, name='create'),
    path('delete/<int:pk>/', views.QuoteDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.QuoteUpdateView, name='update'),
    path('quote/<int:pk>/', views.QuoteDetailVIew.as_view(), name='quote')
]
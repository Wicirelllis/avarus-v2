from django.urls import path, reverse, include
from apps.profiles.models import Profile
from . import views


urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('profile/', views.ProfileView, name='profile'),
    path('', include('django.contrib.auth.urls')),
]

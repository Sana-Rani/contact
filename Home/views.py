from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
def index(request):
    return render(request, 'index.html')
def game(request):
    return render(request, "game.html")
def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.save()
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('index')  # Use redirect after POST to prevent re-submission on refresh
    return render(request, 'index.html')

from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view, name='signup'),
    ]
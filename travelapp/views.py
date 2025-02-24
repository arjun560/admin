from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Home page view
def home(request):
    return render(request, 'home.html')

# User registration view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
 
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'Please fill all the fields')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            # Create and save user
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('login_view')
    
    return render(request, 'login.html')

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')   

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

# User logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login_view')

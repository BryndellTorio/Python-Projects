from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'ecomponents/index.html')

def register(request):

    return render(request, 'ecomponents/register.html')

def my_login(request):

    return render(request, 'ecomponents/my-login.html')

def dashboard(request):

    return render(request, 'ecomponents/dashboard.html')

def profile_management(request):

    return render(request, 'ecomponents/profile-management.html')
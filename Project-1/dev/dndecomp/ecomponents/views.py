from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from .models import Profile
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


def index(request):
    return render(request, "ecomponents/index.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

    if form.is_valid():
        current_user = form.save(commit=False)

        form.save()

        profile = Profile.objects.create(user=current_user)

        return redirect("my-login")

    context = {"form": form}

    return render(request, "ecomponents/register.html", context=context)


def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {"form": form}

    return render(request, "ecomponents/my-login.html", context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("")


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "ecomponents/dashboard.html")


@login_required(login_url="my-login")
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            return redirect("dashboard")

    context = {"user_form": user_form}

    return render(request, "ecomponents/profile-management.html", context=context)


@login_required(login_url="my-login")
def delete_account(request):
    if request.method == "POST":
        delete_user = User.objects.get(username=request.user)

        delete_user.delete()

        return redirect("")

    return render(request, "ecomponents/delete-account.html")

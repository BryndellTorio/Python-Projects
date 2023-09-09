from django.shortcuts import render, redirect


from .forms import CreateUserForm


def index(request):
    return render(request, "ecomponents/index.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")

    context = {"form": form}

    return render(request, "ecomponents/register.html", context=context)


def my_login(request):
    return render(request, "ecomponents/my-login.html")


def dashboard(request):
    return render(request, "ecomponents/dashboard.html")


def profile_management(request):
    return render(request, "ecomponents/profile-management.html")

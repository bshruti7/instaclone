from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import UserSignupForm


def signup_user(request):

    context = {
        "form": UserSignupForm
    }

    return render(request, "users/signup.html", context)


def login_user(request):

    return render(request, 'users/login.html')
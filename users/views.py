from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.contrib.auth.models import User

def signup_user(request):

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                # Create the user with hashed password
                user = User.objects.create_user(username=username, email=email, password=password)
                print("User saved:", user)
            except Exception as e:
                print("Error saving user:", str(e))
            # return redirect('success_page')  # Redirect after successful signup
    else:
        form = UserSignupForm()

    return render(request, 'users/signup.html', {'form': form})


def login_user(request):
    return render(request, 'users/login.html')
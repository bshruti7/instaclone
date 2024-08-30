from django.shortcuts import render, redirect
from .forms import UserSignupForm


def signup_user(request):

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # This saves the user to the database
                print("User saved:", user)
            except Exception as e:
                print("Error saving user:", str(e))
            # return redirect('success_page')  # Redirect after successful signup
    else:
        form = UserSignupForm()

        if form.is_valid():
            try:
                user = form.save()  # This saves the user to the database
                print("User saved:", user)
            except Exception as e:
                print("Error saving user:", str(e))
            # return redirect('success_page')  # Redirect after successful signup

    return render(request, 'users/signup.html', {'form': form})

def login_user(request):
    return render(request, 'users/login.html')
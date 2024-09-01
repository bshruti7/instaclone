from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.messages import get_messages

from .models import UserProfile


def signup_user(request):

    clear_messages(request)

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
                UserProfile.objects.create(user=user)

                # Send verification email
                send_verification_email(user)

                # Redirect to login page
                messages.success(request, 'Account created! Please check your email to verify your account.')
                return redirect('signup')

            except Exception as e:
                print("Error saving user:", str(e))
            # return redirect('success_page')  # Redirect after successful signup
    else:
        form = UserSignupForm()

    return render(request, 'users/signup.html', {'form': form})

def clear_messages(request):
    """Function to clear messages from the request."""
    storage = get_messages(request)
    for _ in storage:
        pass  # Mark messages as used

def send_verification_email(user):
    subject = 'Verify your account'
    message = f'Hi {user.username}, please click the link below to verify your account:'
    verification_link = 'http://instaclone.com/verify/'  # Replace with actual verification link logic
    send_mail(
        subject,
        message + verification_link,
        'passwordverification@instaclone.com',  # Replace with your sender email
        [user.email],
        fail_silently=False,
    )

def login_user(request):
    return render(request, 'users/login.html')
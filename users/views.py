from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserCreateSerializer, UserProfileViewSerializer

from .forms import UserSignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.messages import get_messages
from .models import UserProfile
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken


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


@api_view(['POST'])
def create_user(request):

    serializer = UserCreateSerializer(data=request.data)
    response_data = {
        'errors': None,
        'data': None
    }
    response_status = None

    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        response_data['data'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        response_status = status.HTTP_201_CREATED

    else:

        response_data['errors'] = serializer.errors
        print(response_data)
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data, status=response_status)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_users(request):
    print(request.user.username)

    users = UserProfile.objects.all()

    serialized_data = UserProfileViewSerializer(instance=users, many=True)

    return Response(serialized_data.data, status=status.HTTP_200_OK)



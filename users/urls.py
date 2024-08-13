from django.urls import path
import users.views as users_views

urlpatterns = [
    path("signup/", users_views.signup_user, name="signup"),
    path("login/", users_views.login_user, name="login")
]
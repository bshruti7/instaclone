from django.urls import path
import users.views as users_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path("signup/", users_views.signup_user, name="signup"),
    #path("login/", users_views.login_user, name="login"),
    path("add", users_views.create_user, name="add"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', TokenObtainPairView.as_view(), name='login_api'),

]
from django.urls import path
import users.views as users_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", users_views.signup_user, name="signup"),
    path("add", users_views.create_user, name="add"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', TokenObtainPairView.as_view(), name='login_api'),
    path("viewusers/",users_views.list_users, name="list_users"),
    path("update/", users_views.update_user_profile, name="update_user_profile")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
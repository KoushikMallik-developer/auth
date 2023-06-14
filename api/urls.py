from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.views.all_users import AllUsersView
from api.views.generate_email_otp import GenerateEmailOTPView
from api.views.profile import UserProfileView
from api.views.send_password_reset_email import SendPasswordResetEmailView
from api.views.user_login import UserLoginView
from api.views.user_password_change import UserChangePasswordView
from api.views.user_password_reset import UserPasswordResetView
from api.views.user_registration import UserRegistrationView
from api.views.verify_email import VerifyOTPView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name="User Registration"),
    path('login', UserLoginView.as_view(), name="User Login"),
    path('profile', UserProfileView.as_view(), name="User Profile"),
    path('change_password', UserChangePasswordView.as_view(), name="Change User Password"),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('generate-verification-otp', GenerateEmailOTPView.as_view(), name='generate-verification-otp'),
    path('verify-email', VerifyOTPView.as_view(), name='verify_email'),
    path('get-all-users', AllUsersView.as_view(), name='verify_email'),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

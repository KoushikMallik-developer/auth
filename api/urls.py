from django.urls import path

from api.views.profile import UserProfileView
from api.views.send_password_reset_email import SendPasswordResetEmailView
from api.views.user_login import UserLoginView
from api.views.user_password_change import UserChangePasswordView
from api.views.user_password_reset import UserPasswordResetView
from api.views.user_registration import UserRegistrationView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name="User Registration"),
    path('login', UserLoginView.as_view(), name="User Login"),
    path('profile', UserProfileView.as_view(), name="User Profile"),
    path('change_password', UserChangePasswordView.as_view(), name="Change User Password"),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]

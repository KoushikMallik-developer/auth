from django.urls import path

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

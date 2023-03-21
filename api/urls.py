from django.urls import path

from api.views.user_login import UserLoginView
from api.views.user_registration import UserRegistrationView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name="User Registration"),
    path('login', UserLoginView.as_view(), name="User Registration"),
]

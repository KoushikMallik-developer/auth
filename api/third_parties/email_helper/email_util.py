import logging
import os
import random

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from api.models import User


class EmailUtil:

    @staticmethod
    def _send_email(data):
        if data:
            email = EmailMessage(
                subject=data['subject'],
                body=data['body'],
                from_email=os.environ.get('EMAIL_FROM'),
                to=[data['to_email']]
            )
            try:
                email.send()
            except Exception as e:
                logging.error("Email could not be sent - " + e.__str__())
        else:
            logging.error("Email could not be sent - " + "Necessary Information are not provided.")

    @staticmethod
    def send_verification_email(data: dict) -> str:
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            _otp = ""
            for i in range(6):
                _digit = str(random.randint(a=0, b=9))
                _otp += _digit
            # Send EMail
            body = 'Use this One Time Password to verify your account. - ' + _otp
            data = {
                'subject': 'Verify Your Account',
                'body': body,
                'to_email': user.email
            }
            EmailUtil._send_email(data)
            return _otp
        else:
            raise serializers.ValidationError('You are not a Registered User')

    @staticmethod
    def send_forget_password_email(attrs: dict) -> None:
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():

            user = User.objects.get(email=attrs.get("email"))
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)  # Remove this in Production
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)  # Remove this in Production
            link = '[FrontendBaseURL]' + uid + '/' + token
            print('Password Reset Link', link)  # Remove this in Production
            # Send EMail
            body = 'Click Following Link to Reset Your Password ' + link
            data = {
                'subject': 'Reset Your Password',
                'body': body,
                'to_email': user.email
            }
            EmailUtil._send_email(data)
        else:
            raise serializers.ValidationError('You are not a Registered User')

import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.models.verification import Verification
from api.renderers.json_renderer import UserRenderer


class GenerateEmailOTPView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        try:
            email = request.data.get("email")
            if email and email != "":
                user = User.objects.filter(email=email)
                if user.count() == 1:
                    user = user[0]
                    if not user.get_is_active:
                        _otp = ""
                        for i in range(6):
                            _digit = str(random.randint(a=0, b=9))
                            _otp += _digit
                        verification = Verification.objects.filter(user=user)
                        if verification.count() != 1:
                            verification = Verification(user=user, security_key=_otp)
                        else:
                            verification = verification[0]
                            verification.security_key = _otp
                        verification.save()
                        print(_otp)
                        # send_email_otp()
                        return Response({'msg': 'OTP sent to email.'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'msg': 'User is already verified.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'msg': 'User is not registered.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'msg': 'Please provide valid Email.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': "Some Error Occured - " + str(e.__str__())},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

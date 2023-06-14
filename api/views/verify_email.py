from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.models.verification import Verification
from api.renderers.json_renderer import UserRenderer


class VerifyOTPView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        try:
            email = request.data.get("email")
            _otp = request.data.get("otp")
            if email and email != "":
                if _otp and _otp != "":
                    user = User.objects.filter(email=email)
                    if user.count() == 1:
                        user = user[0]
                    else:
                        return Response({'msg': 'Email is not registered with us.'}, status=status.HTTP_400_BAD_REQUEST)
                    verification = Verification.objects.filter(user=user)
                    if verification.count() == 1:
                        verification = verification[0]
                        if verification.security_key == _otp:
                            verification.user.is_active = True
                            verification.user.save()
                            verification.delete()
                            return Response({'msg': 'Verification successful'}, status=status.HTTP_200_OK)
                        else:
                            return Response({'msg': 'Invalid OTP Provided'}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'msg': 'Please generate verification code first.'},
                                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'msg': 'Please provide valid OTP'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'msg': 'Please provide valid Email'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': "Some Error Occured - " + str(e.__str__())},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

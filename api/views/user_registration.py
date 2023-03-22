from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.user_registration_serializer import UserRegistrationSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        user_reg_serializer = UserRegistrationSerializer(data=request.data)
        if user_reg_serializer.is_valid(raise_exception=True):
            user_reg_serializer.save()
            return Response({"msg": "Registration Successful"}, status=status.HTTP_201_CREATED)
        return Response({"msg": "Registration Failed"}, status=status.HTTP_400_BAD_REQUEST)

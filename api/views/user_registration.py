from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.renderers.json_renderer import UserRenderer
from api.serializers.user_registration_serializer import UserRegistrationSerializer


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        try:
            user_reg_serializer = UserRegistrationSerializer(data=request.data)
            if user_reg_serializer.is_valid(raise_exception=True):
                user_reg_serializer.save()
                # tokens = get_tokens_for_user(user)
                return Response({"msg": "Registration Successful. Please verify your Email."},
                                status=status.HTTP_201_CREATED)
            return Response({"msg": "Registration Failed"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': "Some Error Occured - " + str(e.__str__())},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

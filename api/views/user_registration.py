from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.renderers.json_renderer import UserRenderer
from api.serializers.user_registration_serializer import UserRegistrationSerializer
from api.views.helpers.token_helper import get_tokens_for_user


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        user_reg_serializer = UserRegistrationSerializer(data=request.data)
        if user_reg_serializer.is_valid(raise_exception=True):
            user = user_reg_serializer.save()
            tokens = get_tokens_for_user(user)
            return Response({'tokens': tokens, "msg": "Registration Successful"}, status=status.HTTP_201_CREATED)
        return Response({"msg": "Registration Failed"}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.renderers.json_renderer import UserRenderer
from api.serializers.password_reset_serializer import UserPasswordResetSerializer


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token):
        try:
            serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
            serializer.is_valid(raise_exception=True)
            return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg': "Some Error Occured - " + str(e.__str__())},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

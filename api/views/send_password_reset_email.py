from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.renderers.json_renderer import UserRenderer
from api.serializers.password_reset_email_serializer import SendPasswordResetEmailSerializer


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        try:
            serializer = SendPasswordResetEmailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response({'msg': 'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg': "Some Error Occured - " + str(e.__str__())},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

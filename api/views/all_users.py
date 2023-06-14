from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User


class AllUsersView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            user_details = []
            for user in users:
                user_detail = {
                    "email": user.email,
                    "id": user.id,
                    "username": user.username,
                }
                user_details.append(user_detail)
            return Response({'users': user_details}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg': "Some Error Occured - " + str(e.__str__())},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

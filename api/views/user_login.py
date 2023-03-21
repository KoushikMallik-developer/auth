from rest_framework.response import Response
from rest_framework.views import APIView


class UserLoginView(APIView):
    def post(self, request):
        return Response({"msg": "Login Successful"})

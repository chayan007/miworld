from rest_framework.views import APIView
from users.api.serializers import LoginSerializer
from django.contrib.auth import logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status= 204)
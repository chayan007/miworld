from rest_framework.views import APIView
from users.api.serializers import LoginSerializer
from django.contrib.auth import login as django_login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.valid(raise_exception= True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user)
        return Response({'token' : token.key}, status = 200)
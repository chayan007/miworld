from rest_framework import generics
from rest_framework.response import Response
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication

class RegisterView(generics.CreateAPIView):
    authentication_classes = TokenAuthentication
    permission_classes = AllowAny

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username,email,password)
        token = Token.objects.create(user=user)
        return Response({
            'detail': 'User has been registered',
            'token': token.key
        })


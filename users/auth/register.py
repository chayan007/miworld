from rest_framework import generics, views, status
from rest_framework.response import Response
from users.api.serializers import RegistrationSerializer
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication


class RegisterView(views.APIView):

    @csrf_exempt
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    token = Token.objects.create(user=user)
                    return Response({
                        'detail': 'User has been registered',
                        'token': token.key
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "error": "Wrong API Call Error"
                    })
            else:
                return Response({
                    "error": "Wrong API Call Error"
                })
        except:
            return Response({
                "error": "Wrong API Call Error"
            })

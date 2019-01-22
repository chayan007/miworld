from rest_framework import generics, views, status
from rest_framework.response import Response
from users.api.serializers import RegistrationSerializer
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication

# class RegistrationView(generics.CreateAPIView):
#     authentication_classes = TokenAuthentication
#     permission_classes = AllowAny
#
#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         user = User.objects.create_user(username,email,password)
#         token = Token.objects.create(user=user)
#         return Response({
#             'detail': 'User has been registered',
#             'token': token.key
#         }, status = status.HTTP_201_CREATED)

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
        except:
            return Response({
                "error" : "Wrong API Call Error"
            }, status=status.HTTP_400_BAD_REQUEST)
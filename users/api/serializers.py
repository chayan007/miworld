from rest_framework import serializers
from users.models import *
from django.contrib.auth import *
from django.core import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
        exclude = ('password',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = '__all__'

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username= username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User Account is disabled"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Wrong credentials provided"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password"
            raise exceptions.ValidationError(msg)
        return data

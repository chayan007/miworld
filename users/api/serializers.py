from rest_framework import serializers
from users.models import *
from django.contrib.auth import *
from django.core import exceptions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.validators import UniqueValidator


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


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, min_length=8)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)

    @csrf_exempt
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'], password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')


class LikerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('slug', 'user')

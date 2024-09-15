from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from users.models import UserProfile


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):

        validated_data['password'] = make_password(validated_data['password'])

        user = User.objects.create_user(**validated_data)

        UserProfile.objects.create(user=user)

        return user


class UserViewSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileViewSerializer(ModelSerializer):

    user = UserViewSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'bio', 'profile_pic', 'is_verified')


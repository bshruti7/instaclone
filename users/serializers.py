from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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


class UserProfileUpdateSerializer(ModelSerializer):

    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):

        user = instance.user

        user.first_name = validated_data.pop('first_name')
        user.last_name = validated_data.pop('last_name')

        user.save()

        instance.bio = validated_data['bio']
        instance.save()

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'bio')


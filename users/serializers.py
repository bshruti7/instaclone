from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import UserProfile


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):

        validated_data['password'] = make_password(validated_data['password'])

        user = User.objects.create_user(**validated_data)

        UserProfile.objects.create(user=user)

        return user


class UserViewSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserProfileViewSerializer(ModelSerializer):

    user = UserViewSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'bio', 'profile_pic_url', 'is_verified')


class UserProfileUpdateSerializer(ModelSerializer):

    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'bio', 'profile_pic_url')

    def update(self, instance, validated_data):

        user = instance.user
        user_data = validated_data.get('user')
        validated_data.pop('user')
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()

        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_pic_url = validated_data.get('profile_pic_url', instance.profile_pic_url)
        instance.save()

        return instance

from django.contrib.auth.models import User
from django.db import models


class TimeStamp(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStamp):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True)


# Create your models here.

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
import io
from uuid import uuid4
import os


class TimeStamp(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def validate_image(image):

    limit_kb = 150
    limit_bytes = limit_kb * 1024
    file_size = 0

    if isinstance(image, io.BytesIO):
        file_size = image.getbuffer().nbytes
    elif hasattr(image, 'size'):
        file_size = image.size

    if file_size > limit_bytes:
        raise ValidationError(f"Max size of file is {limit_kb} KB, Current size is {file_size/1024} KB")


def rename_image(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Generate a new filename using UUID
    new_filename = f'{uuid4().hex}.{ext}'
    # Return the new path
    return os.path.join('profile_pics', new_filename)


class UserProfile(TimeStamp):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)
    profile_pic_url = models.ImageField(upload_to=rename_image, blank=True, validators=[validate_image])



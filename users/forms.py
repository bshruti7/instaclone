from django import forms
from .models import User


class UserSignupForm(forms.ModelForm):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    #password = forms.PasswordInput(required=True)


    class Meta:
        model = User
        exclude = ('created_on', 'updated_on', 'is_active')






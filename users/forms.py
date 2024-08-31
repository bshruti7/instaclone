from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


class UserSignupForm(forms.ModelForm):

    username = forms.CharField(required=True, widget=forms.widgets.TextInput(
                                                attrs={
                                                    "placeholder": "Enter your userame",
                                                    "class": "input-fields"
                                            }
    ), label="UserName")
    email = forms.EmailField(required=True, widget=forms.widgets.EmailInput(
                                                attrs={
                                                    "placeholder": "Enter your email",
                                                    "class": "input-fields"
                                                }
    ), label="Email")
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
                                                attrs={
                                                    "placeholder": "Enter your password",
                                                    "class": "input-fields"
                                                }
    ), label="Password")


    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    # def save(self, commit=True):
    #     user = super(UserSignupForm, self).save(commit=False)
    #     # Access the password value and hash it
    #     user.password = make_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user

    def visible_fields(self):
        return [field for field in super().visible_fields() if
                field.name in ['username', 'email', 'password']]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken. Please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered. Please use a different email.")
        return email







from django import forms
from .models import User


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

    def visible_fields(self):
        return [field for field in super().visible_fields() if
                field.name in ['username', 'email', 'password']]







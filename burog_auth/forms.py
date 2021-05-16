from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmailLowerField(forms.EmailField):
    def to_python(self, value):
        return value.lower()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'username__input form__input', 
                'placeholder': 'jonsm'
    }))
    email = forms.EmailField(
        required=True, 
        label='email', 
        widget = forms.EmailInput(
            attrs={
                'class': 'email__input form__input', 
                'placeholder': 'jon@example.com'
    }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password__input form__input', 
                'placeholder': '••••••••••'
    }))

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

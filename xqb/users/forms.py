from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_registration.forms import RegistrationForm

from users.models import Profile


class NewRegistrationForm(RegistrationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'first_name',
            'last_name',
            get_user_model().USERNAME_FIELD,
            get_user_model().get_email_field_name(),
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('That email is already taken.')
        return email


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['timezone']

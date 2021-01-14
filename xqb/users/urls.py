from django.urls import path
from django_registration.backends.activation.views import RegistrationView

from users.forms import NewRegistrationForm
from users.views import update_profile


app_name = 'users'
urlpatterns = [
    path('settings/', update_profile, name='settings'),
    path(
        'register/',
        RegistrationView.as_view(form_class=NewRegistrationForm),
        name='django_registration_register'
    ),
]

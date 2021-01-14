from django.contrib import admin
from django.urls import include, path
from django_js_reverse.views import urls_js

from pages.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('users.urls')),
    path('jsreverse/', urls_js, name='js_reverse'),
    path('martor/', include('martor.urls')),
    path('notes/', include('notes.urls')),
    path('notebooks/', include('notebooks.urls')),
]

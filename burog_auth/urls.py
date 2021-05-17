from django.urls import path
from django.contrib.auth import views as auth_views

from .views import FormWizardView
from .forms import UserAuthForm

urlpatterns = [
    path('register/', FormWizardView.as_view(), name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            form_class=UserAuthForm, template_name='burog_auth/login.html'
        ),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

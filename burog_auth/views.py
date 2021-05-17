import os

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from formtools.wizard.views import SessionWizardView

from .forms import UserRegisterForm, UserDetailsForm


class FormWizardView(SessionWizardView):
    template_name = 'burog_auth/register.html'
    form_list = [UserRegisterForm, UserDetailsForm]
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'profile_pictures')
    )

    def done(self, form_list, form_dict, **kwargs):
        register_form = form_dict['0'].cleaned_data
        detail_form = form_dict['1'].cleaned_data
        user = self.create_user(register_form, detail_form)
        self.create_profile(detail_form, user)
        login(self.request, user)
        return redirect('blog-home')

    def create_user(self, register_form, detail_form):
        user = User(
            username=register_form['username'],
            email=register_form['email'],
            first_name=detail_form['first_name'],
            last_name=detail_form['last_name'],
        )
        user.set_password(register_form['password1'])
        user.save()
        return user

    def create_profile(self, detail_form, user):
        user.profile.image = detail_form['image']
        user.profile.save()

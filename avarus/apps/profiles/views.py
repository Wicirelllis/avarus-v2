from json import dumps

from apps.profiles.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views import generic
from django.contrib import messages
from .forms import RegisterForm, UserEditForm, ProfileEditForm
from apps.datasets.models import Dataset, DatasetRequest

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, 'registration/register.html', {'form': form})


def ProfileView(request):
    user_form = UserEditForm(instance=request.user, data=request.POST)
    profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

    if request.method == 'POST' and user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
    ctx = {
        'profile_form': profile_form,
        'user_form': user_form,
        'available_datasets': Dataset.objects.filter(status='pu').distinct() | Dataset.objects.filter(available_to=request.user).distinct(),
        'requested_datasets': DatasetRequest.objects.all(),
    }
    return render(request, 'registration/profile.html', ctx)

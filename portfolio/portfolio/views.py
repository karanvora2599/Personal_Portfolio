from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import user_passes_test, login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
# from backend.models import *
# from backend.forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# from backend.task import *
# from ckeditor.fields import RichTextField
# from .decorators import *
from django.template.loader import render_to_string








def homepage(request):
    params = {}
    return render(request, 'frontend/index2.html', params)
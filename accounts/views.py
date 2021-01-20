from django.shortcuts import render
from djanog.core.urlresolvers import reverse_lazy
from djanog.views.generic import CreateView

from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
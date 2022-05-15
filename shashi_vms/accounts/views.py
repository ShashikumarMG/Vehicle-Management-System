from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import User
from .forms import UserDataForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
class UsereDataList(generic.CreateView):
    model = User
    form_class = UserDataForm
    template_name = "accounts/user_data.html"
    success_message = "Thank you the form was Submitted Successfully!!!!!!"
    
    def get_success_url(self):
        return reverse_lazy('accounts:user_data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context


class UserUpdate(UpdateView):
    model = User
    form_class = UserDataForm
    template_name = "accounts/user_data.html"

    def get_success_url(self):
        return reverse_lazy('accounts:user_data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context


class DeleteUser(DeleteView):
    model = User
    template_name = "accounts/delete.html"

    def get_success_url(self):
        return reverse_lazy('accounts:user_data')

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import User
from .forms import UserDataForm

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
        # Add in a QuerySet of all the books
        context['user_list'] = User.objects.all()
        # context['user_data'] = self.request.user
        return context
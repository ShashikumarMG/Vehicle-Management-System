from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .model import VihicleData
from .forms import VihicleDataForm

# Create your views here.
class Home(generic.TemplateView):
    model = VihicleData
    form_class = VihicleDataForm
    template_name = "vihicle_data.html"
    success_message = "Thank you the form was Submitted Successfully!!!!!!"
    
    def get_success_url(self):
        return reverse_lazy('accounts:home')
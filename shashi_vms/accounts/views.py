from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# from .forms import StudentForm
# from .models import Student
# Create your views here.
from django.views import generic
class Home(generic.TemplateView):
    # model = Student
    # form_class = StudentForm
    template_name = "index.html"
    # success_message = "Thank you the form was Submitted Successfully!!!!!!"
    
    # def get_success_url(self):
    #     return reverse_lazy('accounts:home')
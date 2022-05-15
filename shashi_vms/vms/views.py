from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import VehicleData
from .forms import VehicleDataForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


# Create your views here.
class VehicleDataList(generic.CreateView):
    model = VehicleData
    form_class = VehicleDataForm
    template_name = "vihicle_data.html"
    success_message = "Thank you the form was Submitted Successfully!!!!!!"
    
    def get_success_url(self):
        return reverse_lazy('vms:vihicle')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['vehicle_list'] = VehicleData.objects.all()
        context['user_data'] = self.request.user
        return context


class UserUpdate(UpdateView):
    model = VehicleData
    form_class = VehicleDataForm
    template_name = "vihicle_data.html"

    def get_success_url(self):
        return reverse_lazy('vms:vihicle')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle_list'] = VehicleData.objects.all()
        return context


class DeleteUser(DeleteView):
    model = VehicleData
    template_name = "accounts/delete.html"

    def get_success_url(self):
        return reverse_lazy('vms:vihicle')

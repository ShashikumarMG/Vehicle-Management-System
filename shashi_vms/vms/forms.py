from django import forms
from .models import VehicleData

class VehicleDataForm(forms.ModelForm):

    class Meta:
        model = VehicleData
        fields = '__all__'
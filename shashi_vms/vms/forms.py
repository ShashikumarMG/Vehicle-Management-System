from django import forms
from .model import VihicleData

class VihicleDataForm(forms.ModelForm):

    class Meta:
        model = VihicleData
        fields = '__all__'
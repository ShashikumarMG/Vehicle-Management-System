from django import forms
from .models import User


class UserDataForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    conformpassword = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['email','username','groups','first_name','last_name','password','conformpassword']
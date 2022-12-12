from django import forms
from django.contrib.auth.models import User
from . import models


class AccoutnForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['user_name', 'name', 'balance']

        widgets = {
            'user_name':forms.TextInput(attrs={'class':'form-control'}),
            'owner' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
        }

class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = ['name']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }
        
from django import forms
from .models import *

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['products']
        fields = '__all__'
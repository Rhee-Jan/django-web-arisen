from django import forms

from .models import alumni
from django.core.exceptions import ValidationError



class alumniForm(forms.ModelForm):
    class Meta:
        model = alumni
        fields = ["first_name","last_name","gender","age"]
from django import forms
from .models import register

class registerform(forms.ModelForm):
    class Meta:
        model = register
        fields = ['first_name', 'last_name', 'mobile', 'place']

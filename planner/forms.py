from django import forms
from .models import Planner

class PlannerForm(forms.ModelForm):
    class Meta:
        model=Planner
        fields={'title','text','author','created_date',}
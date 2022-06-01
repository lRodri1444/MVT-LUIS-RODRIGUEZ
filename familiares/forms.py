from django import forms
from django.forms import ModelForm
from .models import Persona


#Widgets

class DateInput(forms.DateInput):
    input_type = 'date'

#Forms

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {'birth_date':DateInput}
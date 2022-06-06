from django import forms
from django.forms import ModelForm
from .models import Persona, Job, Migration


#Widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class CheckBoxInput(forms.CheckboxInput):
    input_type = 'checkbox'

#Forms

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {'birth_date':DateInput}

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class MigrationForm(ModelForm):
    class Meta:
        model = Migration
        fields = '__all__'
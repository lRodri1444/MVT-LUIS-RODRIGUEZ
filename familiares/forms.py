from django import forms
from django.forms import ModelForm
from .models import Persona, Job, Migration

#Widgets

def placeholder(reference_text):                                   #(string)
    ref = forms.TextInput(attrs={'placeholder':reference_text})
    return ref

def numeric_placeholder(reference_text, number_limit):             #(string,integer)
    ref_lim = forms.NumberInput(attrs={
        'placeholder':reference_text,
        'onKeyPress':f'if(this.value.length=={number_limit}) return false;'
    })
    return ref_lim

class DateInput(forms.DateInput):
    input_type = 'date'

#Forms

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'birth_date':DateInput,
            'name': placeholder('i.e. Marcos Antonio'),
            'surname': placeholder('i.e. Hernandez Quispe'),
            'document_id': numeric_placeholder('i.e. 12345678', 8),
            'phone_number': numeric_placeholder('i.e. 123456789', 9)
        }

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {'health_insurance':numeric_placeholder('i.e. 123456789', 9)}

class MigrationForm(ModelForm):
    class Meta:
        model = Migration
        fields = '__all__'
        widgets = {'passport_id':numeric_placeholder('i.e. 123456789', 9)}
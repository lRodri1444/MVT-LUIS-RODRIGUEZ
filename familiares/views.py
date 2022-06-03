from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonaForm
from .models import Persona

def index(request):
    form = PersonaForm()
    if request.method == 'POST':
        print(request.POST)
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'familiares/data.html',{'form':form})

def filter_input(request):
    personas = Persona.objects.all()
    phonenum = request.GET.get('phonenum')    
    if phonenum:
        personas = personas.filter(phone_number = phonenum)
        template_name = 'familiares/filter_results.html'
    else:
        template_name = 'familiares/filter.html'
    return render(request, template_name,{'personaskey':personas, 'phonefiltro':phonenum})
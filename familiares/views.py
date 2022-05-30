from django.shortcuts import render
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

def db(request):
    filtro = Persona.objects.all()
    return render(request, 'familiares/filter.html',{'family_data':filtro})
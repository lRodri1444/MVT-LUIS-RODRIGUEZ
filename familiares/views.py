from django.shortcuts import render
from django.http import HttpResponse
from .models import persona

def home(request):
    context = {
        'info':persona.objects.all()
    }
    return render(request, 'familiares/data.html', context)


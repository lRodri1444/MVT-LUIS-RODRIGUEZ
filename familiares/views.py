from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain
from .forms import PersonaForm, JobForm, MigrationForm
from .models import Persona, Job, Migration

def index(request):
    form = PersonaForm()
    jobform = JobForm()
    migrationform = MigrationForm()

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        jobform = JobForm(request.POST)
        migrationform = MigrationForm(request.POST)
        if form.is_valid() and jobform.is_valid() and migrationform.is_valid():
            form.save()
            jobform.save()
            migrationform.save()

    context = {
        'form':form,
        'jobform':jobform,
        'migrationform':migrationform
    }

    return render(request,'familiares/data.html', context)

def filter_input(request):
    personas = Persona.objects.all()
    jobs = Job.objects.all()
    migrations = Migration.objects.all()

    documentnum = request.GET.get('documentnum')
    hinum = request.GET.get('hinum')
    pspnum = request.GET.get('pspnum')

    if documentnum and hinum and pspnum:
        personas = personas.filter(document_id = documentnum)
        jobs = jobs.filter(health_insurance = hinum)
        migrations = migrations.filter(passport_id = pspnum)
        template_name = 'familiares/filter_results.html'
    else:
        template_name = 'familiares/filter.html'

    context = {
        'personaskey':personas,
        'jobskey':jobs,
        'migrationskey':migrations,

        'documentfiltro':documentnum,
        'hifiltro':hinum,
        'pspfiltro':pspnum
    }

    return render(request, template_name, context)
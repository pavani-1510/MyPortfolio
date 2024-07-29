from django.shortcuts import render
from .models import Project, Certification

def home(request):
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    context = {
        'projects': projects,
        'certifications': certifications
    }
    return render(request, 'home.html', context)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications.html', {
        'certifications': certifications
    })

from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    skills = Skill.objects.all()
    return render(request, 'index.html', {
        'skills': skills,
    })

def project(request, project_slug):
    return HttpResponse(f'<p>project view with slug {project_slug}</p>')

def projects(request):
    return HttpResponse('<p>projects view</p>')

def experiences(request):
    return HttpResponse('<p>experiences view</p>')

def educations(request):
    return HttpResponse('<p>educations view</p>')

def skill_detail(request, skill_id):
    try:
        skill = Skill.objects.get(id=skill_id)
    except Skill.DoesNotExist:
        raise Http404('Skill not found')
    return render(request, 'skill_detail.html', {'skill': skill})

@login_required(login_url='/admin')
def authorised(request):
    return render(request, 'authorised.html', {})

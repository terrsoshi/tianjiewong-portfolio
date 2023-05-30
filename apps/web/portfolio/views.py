from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'skills': Skill.objects.all()}

class SkillsView(ListView):
    model = Skill
    context_object_name = "skills"
    template_name = 'skills.html'

def project(request, project_slug):
    return HttpResponse(f'<p>project view with slug {project_slug}</p>')

def projects(request):
    return HttpResponse('<p>projects view</p>')

def experiences(request):
    return HttpResponse('<p>experiences view</p>')

def educations(request):
    return HttpResponse('<p>educations view</p>')

class SkillDetailView(DetailView):
    model = Skill
    context_object_name = "skill"
    template_name ='skill_detail.html'

class AuthorisedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorised.html'
    login_url = '/admin'

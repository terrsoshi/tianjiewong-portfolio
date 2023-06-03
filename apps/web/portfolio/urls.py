from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/<str:project_slug>/', views.project, name='project'),
    path('projects/', views.projects, name='projects'),
    path('experiences/', views.experiences, name='experiences'),
    path('educations/', views.educations, name='educations'),
    path('skills/<int:pk>/', views.SkillDetailView.as_view(), name='skill'),
    path('authorised/', views.AuthorisedView.as_view(), name='authorised'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    # Login View
    path('login/', api_views.LoginView.as_view(), name='login'),
    # RESTful APIs
    path('api/projects/', api_views.ProjectListAPIView.as_view(), name='project-list'),
    path('api/projects/create/', api_views.ProjectCreateAPIView.as_view(), name='project-create'),
    path('api/projects/<int:id>/', api_views.ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-retrieve-update-destroy'),
    path('api/skills/', api_views.SkillListAPIView.as_view(), name='skill-list'),
    path('api/skills/<int:id>/', api_views.SkillRetrieveAPIView.as_view(), name='skill-retrieve'),
    path('api/experiences/', api_views.ExperienceListAPIView.as_view(), name='experiences-list'),
    path('api/educations/', api_views.EducationListAPIView.as_view(), name='educations-list'),
]

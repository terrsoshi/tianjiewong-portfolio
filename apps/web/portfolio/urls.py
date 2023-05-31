from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/<str:project_slug>/', views.project, name='project'),
    path('projects/', views.projects, name='projects'),
    path('experiences/', views.experiences, name='experiences'),
    path('educations/', views.educations, name='educations'),
    path('skills/<int:pk>/', views.SkillDetailView.as_view(), name='skill'),
    path('authorised/', views.AuthorisedView.as_view(), name='authorised'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('secondskills/', views.SkillsView.as_view(), name='secondskills'),
]

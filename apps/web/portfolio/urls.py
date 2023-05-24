from django.urls import path

url_patterns = [
    path('', views.index, name='index'),
    path('project/<str:project_slug>/', views.project, name='project'),
    path('projects/', views.projects, name='projects'),
    path('experiences/', views.experiences, name='experiences'),
    path('educations/', views.educations, name='educations'),
    path('skill_detail/<str:skill_id>/', views.skill_detail, name='skill_detail'),
    path('authorised/', views.authorised, name='authorised')
]
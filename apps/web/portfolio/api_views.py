
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *

class LimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10

class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('current',)
    search_fields = ('title', 'description', 'skills__name')
    ordering_fields = ('id', 'end_date', 'start_date')
    ordering = ('-end_date', '-start_date')
    pagination_class = LimitPagination

class ProjectCreateAPIView(CreateAPIView):
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    
    def delete(self, request, *args, **kwargs):
        project_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete(f'project_data_{project_id}')
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            project = response.data
            cache.set(f'project_data_{project["id"]}', {
                'title': project['title'],
                'description': project['description'],
                'slug': project['slug'],
                'start_date': project['start_date'],
                'end_date': project['end_date'],
                'current': project['current'],
                'link_github': project['link_github'],
                'link_project': project['link_project'],
                'logo': project['logo'],
                'skills': project['skills'],
            })
        return response


from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import login

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import response, status, views, permissions

from .serializers import *
from .models import *

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(None, status=status.HTTP_202_ACCEPTED)

class LimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10

class ProjectListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
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

class SkillListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('category', 'priority',)
    search_fields = ('name',)
    ordering_fields = ('id', 'priority', 'category')
    ordering = ('category', 'priority', 'id')

class SkillRetrieveAPIView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SkillSerializer
    
    def get(self, request, id):
        queryset = Skill.objects.filter(id=id).first()
        if queryset:
            return response.Response(self.serializer_class(queryset).data)
        return response.Response("Skill not found.", status=status.HTTP_404_NOT_FOUND)

class ExperienceListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('current',)
    search_fields = ('title', 'description', 'location', 'institution', 'skills__name')
    ordering_fields = ('id', 'end_date', 'start_date')
    ordering = ('-end_date', '-start_date')
    pagination_class = LimitPagination

class EducationListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('current',)
    search_fields = ('title', 'description', 'location', 'institution', 'subjects__name')
    ordering_fields = ('id', 'grade', 'end_date', 'start_date')
    ordering = ('-end_date', '-start_date')
    pagination_class = LimitPagination
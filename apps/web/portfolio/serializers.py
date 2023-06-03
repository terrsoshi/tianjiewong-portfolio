from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with validate.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, data):
        username = data['username']
        password = data['password']

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        data['user'] = user
        return data

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
    
    title = serializers.CharField(min_length=2, max_length=200)
    description = serializers.CharField(min_length=2)
    slug = serializers.SlugField(read_only=True, max_length=255, validators=[UniqueValidator(queryset=Project.objects.all())])
    start_date = serializers.DateField(
        input_formats = ['%d-%m-%Y', '%Y-%m-%d'],
        help_text = 'Accepted format: DD-MM-YYYY or YYYY-MM-DD',
        style = {'input_type': 'text', 'placeholder': '01-06-2023 or 2023-06-01'},
    )
    end_date = serializers.DateField(
        input_formats = ['%d-%m-%Y', '%Y-%m-%d'],
        help_text = 'Accepted format: DD-MM-YYYY or YYYY-MM-DD',
        style = {'input_type': 'text', 'placeholder': '15-07-2023 or 2023-07-15'},
        required = False,
        allow_null = True,
        default =None,
    )
    current = serializers.BooleanField(default=False)
    link_github = serializers.URLField(required=False)
    link_project = serializers.URLField(required=False)
    logo = serializers.ImageField(required=False)
    skills = SkillSerializer(required=False, many=True)

    def validate(self, data):
        to_assign = slugify(data['title'])
        if Project.objects.filter(slug=to_assign).exists():
            count = 1
            to_assign = slugify(data['title']) + f"-{count}"
            while Project.objects.filter(slug=to_assign).exists():
                count += 1
                to_assign = slugify(data['title']) + f"-{count}"
        data['slug'] = to_assign

        if data['end_date'] is not None:
            if data['start_date'] > data['end_date']:
                raise serializers.ValidationError("Start date must be before end date!")
            elif data['end_date'] >= timezone.now().date():
                data['current'] = True
            else:
                data['current'] = False
        else:
            data['current'] = True
        return data


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
    
    skills = SkillSerializer(required=False, many=True)

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
    
    semester = SemesterSerializer()
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

    subjects = SubjectSerializer(required=False, many=True)

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"
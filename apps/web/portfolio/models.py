from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from datetime import date

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, default=None)
    current = models.BooleanField(default=False)
    link_github = models.URLField(blank=True)
    link_project = models.URLField(blank=True)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    skills = models.ManyToManyField('Skill')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        to_assign = slugify(self.title)

        if Project.objects.filter(slug=to_assign).exists():
            to_assign += f"-{str(Project.objects.filter(slug=to_assign).count())}"
        self.slug = to_assign   

        if self.start_date < self.end_date:
            raise ValueError("Start date must be before end date!")
        if self.end_date is None or self.end_date > date.today():
            self.current = True
        else:
            self.current = False
        
        super().save(*args, **kwargs)

class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    CATEGORY_CHOICES = [('S', 'Tool'), ('L', 'Language'), ('T', 'Technology')]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, default=None)
    current = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    link = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.institution}"
    
    def save(self, *args, **kwargs):
        if self.start_date < self.end_date:
            raise ValueError("Start date must be before end date!")
        if self.end_date is None or self.end_date > date.today():
            self.current = True
        else:
            self.current = False
        
        super().save(*args, **kwargs)

class Education(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, default=None)
    current = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    link = models.URLField(blank=True)
    grade = models.CharField(max_length=200)
    subjects = models.ManyToManyField('Subject')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.institution}"
    
    def save(self, *args, **kwargs):
        if self.start_date < self.end_date:
            raise ValueError("Start date must be before end date!")
        if self.end_date is None or self.end_date > date.today():
            self.current = True
        else:
            self.current = False
        
        super().save(*args, **kwargs)

class Subject(models.Model):
    name = models.CharField(max_length=200)
    semester = models.ForeignKey('Semester', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Semester(models.Model):
    number = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"Semester {str(self.number)}"

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} from {self.name}"
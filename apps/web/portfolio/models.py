from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from datetime import date
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, default=None, blank=True)
    current = models.BooleanField(default=False)
    link_github = models.URLField(blank=True)
    link_project = models.URLField(blank=True)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        to_assign = slugify(self.title)

        if Project.objects.filter(slug=to_assign).exists():
            count = 1
            to_assign = slugify(self.title) + f"-{count}"
            while Project.objects.filter(slug=to_assign).exists():
                count += 1
                to_assign = slugify(self.title) + f"-{count}"
        self.slug = to_assign

        if self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValueError("Start date must be before end date!")
            elif self.end_date >= timezone.now().date():
                self.current = True
            else:
                self.current = False
        else:
            self.current = True

        super().save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=200)
    CATEGORY_CHOICES = [('S', 'Tool'), ('L', 'Language'), ('T', 'Technology')]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    priority = models.IntegerField(default=4, blank=True)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['category', 'priority', 'id']

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, default=None, blank=True)
    current = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    link = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.institution}"

    def save(self, *args, **kwargs):
        if self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValueError("Start date must be before end date!")
            elif self.end_date >= timezone.now().date():
                self.current = True
            else:
                self.current = False
        else:
            self.current = True

        super().save(*args, **kwargs)


class Education(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, default=None, blank=True)
    current = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    logo = CloudinaryField("Image", overwrite=True, format="jpg", blank=True)
    link = models.URLField(blank=True)
    grade = models.CharField(max_length=200)
    subjects = models.ManyToManyField('Subject', blank=True)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.institution}"

    def save(self, *args, **kwargs):
        if self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValueError("Start date must be before end date!")
            elif self.end_date >= timezone.now().date():
                self.current = True
            else:
                self.current = False
        else:
            self.current = True

        super().save(*args, **kwargs)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    semester = models.ForeignKey(
        'Semester', on_delete=models.RESTRICT, null=True)

    class Meta:
        ordering = ['semester', 'name']

    def __str__(self):
        return self.name


class Semester(models.Model):
    number = models.IntegerField(default=1)
    education = models.ForeignKey(
        'Education', on_delete=models.RESTRICT, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['education', 'number']

    def __str__(self):
        return f"Semester {str(self.number)} - {str(self.education)}"


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} from {self.name}"

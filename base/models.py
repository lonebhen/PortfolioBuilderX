from django.db import models
from django.contrib.auth.models import AbstractUser
import re

# Create your models here.

Ratings_range = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    
]


class User(AbstractUser):
    pass


class InformationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email= models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    # avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    CV = models.FileField(upload_to="cv/", blank=True, null=True)



    facebook = models.URLField(blank=True, null=False)
    instagram = models.URLField(blank=True, null=False)
    # snapchat = models.URLField(blank=True, null=False)
    github = models.URLField(blank=True, null=False)
    linkedin = models.URLField(blank=True, null=False)
    other = models.URLField(blank=True, null=False)


    def __str__(self):
        return self.firstName
    

class EducationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    institute = models.CharField(max_length=50, blank = True, null=True)
    description = models.TextField(blank=True, null=False)


    class Meta:
        ordering = ['-year']


    def __str__(self):
        return f"{self.user} => {self.title} from {self.institute}"
    

class ExperienceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    institute = models.CharField(max_length=50, blank = True, null=True)
    description = models.TextField(blank=True, null=False)


    class Meta:
        ordering = ['-year']


    def __str__(self):
        return f"{self.user} => {self.title} from {self.institute}"
    

class SkillSetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    imagelink = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=False)
    skillrank = models.CharField(choices=Ratings_range, default='2', max_length=10)


    class Meta:
        ordering = ['-skillrank']


    def __str__(self):
        return f"{self.user} => {self.title}"


class ProjectModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    imagelink = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=False)
    project_ratings = models.CharField(choices=Ratings_range, default='3', max_length=10)
    demo = models.URLField(blank=True, null=False)
    github_link = models.URLField(blank=True, null=True)


    class Meta:
        ordering = ['-project_ratings']


    def __str__(self):
        return f"{self.user} => {self.title}"
    

    def get_project_absolute_url(self):
        return "/projects/{}".format(self.slug)
    

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(ProjectModel, self).save(*args, **kwargs)

    def slug_generate(self):
        slug = self.title.strip()
        slug = re.sub("", "_", slug)
        return slug.lower()
    


class MessageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=False)
    email = models.EmailField(max_length=45, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    subject = models.CharField(max_length=5000, blank=False, null=False)
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    class Meta:
        ordering = ['-send_time']


    def __str__(self):
        return f"{self.user} => {self.subject}"







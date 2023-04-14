from django import forms
from django.db.models import fields
from .models import (User, InformationModel, EducationModel, ExperienceModel, SkillSetModel, ProjectModel, MessageModel)


class IntroForm(forms.ModelForm):
    class Meta:
        model = InformationModel
        fields = "__all__"


class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = ["title", "year", "institute", "description"]
        labels = {'title': 'Level of Education', 'year': "Year", 'institute': "Institute" }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = ["title", "year", "institute", "description"]
        labels = {'title': 'Position', 'year': "Year", 'institute': "Company Name" }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        #fields= "__all__" 
        exclude = ('user', )


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields=['name', 'email', 'message', 'subject']

class SkillSetForm(forms.ModelForm):
    class Meta:
        model = SkillSetModel
        fields = "__all__"
     

class ContactForm(forms.Form):
    name = forms.CharField(max_length =50)
    email = forms.EmailField(max_length = 100)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
    subject  = forms.CharField(widget=forms.Textarea, max_length=40)

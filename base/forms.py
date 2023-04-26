from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import (User, InformationModel, EducationModel, ExperienceModel, SkillSetModel, ProjectModel, MessageModel)


class IntroForm(ModelForm):
    class Meta:
        model = InformationModel
        fields = "__all__"


    def save(self, commit = True, *args, **kwargs):
        request = None

        if kwargs.__contains__('request'):
            request = kwargs.pop('request')

        m = super(IntroForm, self).save(commit = False, *args, **kwargs)

        if m.user is None and request is not None:
            m.user = request.user
            m.save()


class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = ["title", "year", "institute", "description"]
        labels = {'title': 'Level of Education', 'year': "Year", 'institute': "Institute" }

    def save(self, commit = True, *args, **kwargs):
        request = None

        if kwargs.__contains__('request'):
            request = kwargs.pop('request')

        m = super(EducationForm, self).save(commit = False, *args, **kwargs)

        if m.user is None and request is not None:
            m.user = request.user
            m.save()


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = ["title", "year", "institute", "description"]
        labels = {'title': 'Position', 'year': "Year", 'institute': "Company Name" }


    def save(self, commit = True, *args, **kwargs):
        request = None

        if kwargs.__contains__('request'):
            request = kwargs.pop('request')

        m = super(ExperienceForm, self).save(commit = False, *args, **kwargs)

        if m.user is None and request is not None:
            m.user = request.user
            m.save()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        #fields= "__all__" 
        exclude = ('user', )

    def save(self, commit = True, *args, **kwargs):
        request = None

        if kwargs.__contains__('request'):
            request = kwargs.pop('request')

        m = super(ProjectForm, self).save(commit = False, *args, **kwargs)

        if m.user is None and request is not None:
            m.user = request.user
            m.save()


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields=['name', 'email', 'message', 'subject']

    def save(self, commit = True, *args, **kwargs):
        request = None

        if kwargs.__contains__('request'):
            request = kwargs.pop('request')

        m = super(MessageForm, self).save(commit = False, *args, **kwargs)

        if m.user is None and request is not None:
            m.user = request.user
            m.save()

class SkillSetForm(forms.ModelForm):
    class Meta:
        model = SkillSetModel
        # fields = "__all__"
        exclude = ('user',)

    def save(self, commit = True, *args, **kwargs):
        request = None

        if kwargs.__contains__('request'):
            request = kwargs.pop('request')

        m = super(SkillSetForm, self).save(commit = False, *args, **kwargs)

        if m.user is None and request is not None:
            m.user = request.user
            m.save()
     

class ContactForm(forms.Form):
    name = forms.CharField(max_length =50)
    email = forms.EmailField(max_length = 100)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
    subject  = forms.CharField(widget=forms.Textarea, max_length=40)

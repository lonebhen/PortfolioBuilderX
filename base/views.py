from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse, Http404,JsonResponse,HttpResponseRedirect
from .models import (User, InformationModel, EducationModel, ExperienceModel, SkillSetModel, ProjectModel, MessageModel)
from .forms import (IntroForm, EducationForm, ExperienceForm, SkillSetForm, MessageForm, ProjectForm, ContactForm)

# Create your views here.

def form_createView(request, *args, **kwargs):
    template_name = 'interface/create.html'
    context = {}


    intro_form = IntroForm(request.POST or None)
    if intro_form.is_valid():
        intro_form.save()
    else:
        intro_form = IntroForm

    edu_form = EducationForm(request.POST or None)
    if edu_form.is_valid():
        edu_form.save()
    else:
        edu_form = EducationForm

    exp_form = ExperienceForm(request.POST or None)
    if exp_form.is_valid():
        exp_form.save()
    else:
        exp_form = ExperienceForm

    
    skill_form = SkillSetForm(request.POST or None)
    if skill_form.is_valid():
        skill_form.save()
    else:
        skill_form = SkillSetForm

    
    project_form = ProjectForm(request.POST or None)
    if project_form.is_valid():
        project_form.save()
    else:
        intro_form = ProjectForm



    context = {
        'introFORM': intro_form,
        'expFORM': exp_form,
        'eduFORM': edu_form,
        'projectFORM': project_form,
        'skillFORM': skill_form,
    }

    return render(request, template_name, context)




























































def index(request):
    return render(request, template_name='interface/index.html')


def login_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)


        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
        return render(request, "interface/loginRegister.html", {"message": "Invalid Credentials"})
    
    else:
        return render(request, "interface/loginRegister.html")
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]


        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "interface/loginRegister.html", {"message": "Passwords do not match! Try again"})
        

        try:
            user = User.objects.create_user(username,email,password)
            user.save()
        except IntegrityError:
            return render(request, "interface/loginRegister.html", {"message": "Username already exists"})
        
        login(request, user)

        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, "interface/loginRegister.html")




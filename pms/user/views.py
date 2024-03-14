from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.forms import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, TemplateView
from .models import User
from .forms import ManagerRegistrationForm, DeveloperRegistrationForm
from django.http import HttpRequest, HttpResponse
#import settings.py
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from project.models import Project,Task, ProjectModule
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.utils import timezone
from datetime import datetime, timedelta


class ManagerRegisterView(CreateView):
    template_name = 'user/manage_register.html'
    model = User
    form_class = ManagerRegistrationForm
    success_url = '/user/login/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        print("email-->", email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
        


class DeveloperRegisterView(CreateView):
    template_name = 'user/developer_register.html'
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/user/login/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        print("email-->", email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
        
        
def sendMail(to):
    subject = 'Welcome to pms'
    message = 'Hope you are enjoying django tutorials'
    # recepientList = ["vermasaurabh0204@gmail.com"]
    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject, message, EMAIL_FROM, recepientList)
    #attach file
    #html
    # return HttpResponse("Email Sent")
    return True

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    model = User

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager-dashboard/'
            else:
                return '/user/developer-dashboard/'
        else:
            messages.error(self.request, 'Invalid username or password. Please register first.')


# RESTRICTING DEVELOPER FROM ACCESSING MANAGER DASHBOARD
def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_manager: 
            return redirect(reverse('developer-dashboard')) # Redirect to an access denied page or another appropriate page
        return view_func(request, *args, **kwargs)
    return wrapper    

@method_decorator(manager_required, name='dispatch')
@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class ManagerDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #logic to get all projects    
        context = {}
        total_projects = Project.objects.all().count()
        total_modules = ProjectModule.objects.all().count()
        total_tasks = Task.objects.all().count()
        total_users = User.objects.count()
        projects = Project.objects.all() #select * from employee
        tasks = Task.objects.all()
        context["projects"] = projects
        context["tasks"] = tasks
        context["total_projects"] = total_projects
        context["total_modules"] = total_modules
        context["total_tasks"] = total_tasks
        context["total_users"] = total_users
        return render(request, 'user/manager_dashboard.html', context)
    
    template_name = 'user/manager_dashboard.html'
    
# RESTRICTING MANAGER FROM ACCESSING DEVELOPER DASHBOARD
def developer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_developer:
            return redirect(reverse('manager-dashboard')) # Redirect to an access denied page or another appropriate page
        return view_func(request, *args, **kwargs)
    return wrapper

@method_decorator(developer_required, name='dispatch')
@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class DeveloperDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #logic to get all projects
        context = {}
        tasks = Task.objects.all().values() #select * from employee
        context["tasks"] = tasks
        return render(request, 'user/developer_dashboard.html', context)
    
    template_name = 'user/developer_dashboard.html'
    
class UserListView(ListView):
    template_name = 'user/user_list.html'
    model = User
    context_object_name = 'users'


class UserProfileView(DetailView):
    template_name = 'user/user_profile.html'
    model = User
    context_object_name = 'user_info'
    
    
class ReportView(TemplateView):
    template_name = 'user/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_tasks = Task.objects.filter(status='Completed')

        report_data = []
        for task in completed_tasks:
            estimated_hours = task.hours
            completion_time = timedelta(hours=estimated_hours)
            report_data.append({
                'project_name': task.project,
                'task_name': task.title,
                'task_completion_date': timezone.now().date(),
                'estimated_hours': estimated_hours,
                'actual_hours': completion_time.total_seconds() / 3600
            })

        context['report_data'] = report_data
        return context
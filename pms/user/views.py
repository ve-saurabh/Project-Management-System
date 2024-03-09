from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.forms import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
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
from project.models import Project
from django.contrib import messages
# Create your views here.
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
    success_url = '/login/'

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
    
@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class ManagerDashboardView(ListView):

    def get(self, request, *args, **kwargs):
        #logic to get all projects    
        context = {}
        projects = Project.objects.all().values() #select * from employee
        context["projects"] = projects
        return render(request, 'user/manager_dashboard.html', context)
    
    template_name = 'user/manager_dashboard.html'

class DeveloperDashboardView(ListView):

    def get(self, request, *args, **kwargs):
        #logic to get all projects
        return render(request, 'user/developer_dashboard.html')
    
    template_name = 'user/developer_dashboard.html'
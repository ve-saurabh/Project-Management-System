from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import ProjectCreationForm, ProjectTeamCreationForm, ProjectModuleCreationForm, ProjectTaskCreationForm
from .models import Project, ProjectTeam, ProjectModule, Task
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class ProjectCreationView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'
    # print(Project.objects.all())

@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = "project/project_detail.html"

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = "/project/list/"
    template_name = "project/update_project.html"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete_project.html'
    success_url = "/project/list/"

class ProjectTeamCreateView(CreateView):
    template_name = 'project/create_team.html'
    model = ProjectTeam
    form_class = ProjectTeamCreationForm
    success_url = "/project/list/"


# Project Module view
class ProjectModuleCreateView(CreateView):
    model = ProjectModule
    template_name = 'project/project_module.html'
    form_class = ProjectModuleCreationForm
    success_url = '/project/module_list/'

class ProjectModuleListView(ListView):
    template_name = 'project/module_list.html'
    model = ProjectModule
    context_object_name = 'modules'
 
class ProjectModuleUpdateView(UpdateView):
    template_name = 'project/update_module.html'
    model = ProjectModule
    form_class = ProjectModuleCreationForm
    success_url = '/project/module_list/'

class ProjectModuleDeleteView(DeleteView):
    model = ProjectModule
    template_name = 'project/delete_module.html'
    success_url = '/project/module_list/'


# Task View 
class ProjectTaskCreateView(CreateView):
    model = Task
    form_class = ProjectTaskCreationForm
    template_name = 'project/project_task.html'
    success_url = '/project/task_list/'

class ProjectTaskListView(ListView):
    model = Task
    template_name = 'project/task_list.html'
    context_object_name = "tasks"

class ProjectTaskUpdateView(UpdateView):
    model = Task
    form_class = ProjectTaskCreationForm
    template_name = 'project/update_task.html'
    success_url = '/project/task_list/'

class ProjectTaskDeleteView(DeleteView):
    model = Task
    template_name = 'project/delete_task.html'
    success_url = '/project/task_list/'

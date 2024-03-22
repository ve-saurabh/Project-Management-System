from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import ProjectCreationForm, ProjectTeamCreationForm, ProjectModuleCreationForm, ProjectTaskCreationForm, UserTaskCreationForm
from .models import Project, ProjectTeam, ProjectModule, Task, UserTask
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context[self.context_object_name]
        paginator = Paginator(queryset, settings.PER_PAGE)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

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
    
    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, pk=project_id)
        initial['project'] = project
        return initial


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context[self.context_object_name]
        paginator = Paginator(queryset, settings.PER_PAGE)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
 
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
    
class ProjectTaskAssignView(CreateView):
    model = UserTask
    form_class = UserTaskCreationForm
    template_name = 'project/assign_task.html'
    success_url = '/project/task_list/'
    def get_initial(self):
        initial = super().get_initial()
        task_id = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        initial['task'] = task
        return initial

class UpdateTaskStatus(View):
    def post(self,request,pk):
        task = Task.objects.get(id=pk)

        if task.status == "Not Started":
            task.status = "In Progress"
        elif task.status == "In Progress":
            task.status = "Completed"
        else:
            task.status = "Not Started"

        task.save()

        return redirect(reverse('developer-dashboard'))
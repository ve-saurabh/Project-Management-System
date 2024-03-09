from django.contrib import admin
from django.urls import path
from .views import ProjectCreationView,ProjectListView,ProjectDetailView,ProjectUpdateView,ProjectDeleteView, ProjectTeamCreateView
from .views import ProjectModuleCreateView, ProjectModuleListView, ProjectModuleUpdateView, ProjectModuleDeleteView
from .views import ProjectTaskCreateView, ProjectTaskListView, ProjectTaskUpdateView, ProjectTaskDeleteView
urlpatterns = [
    path("create/", ProjectCreationView.as_view(), name="create"),
    path('list/', ProjectListView.as_view(), name="list"),
    path("project_detail/<int:pk>/",ProjectDetailView.as_view(),name="project_detail"),
    path("update_project/<int:pk>/",ProjectUpdateView.as_view(),name="update_project"),
    path("delete_project/<int:pk>/",ProjectDeleteView.as_view(), name="delete_project"),
    path("create_team/", ProjectTeamCreateView.as_view(), name="project_team_create"),
    path("create_module/", ProjectModuleCreateView.as_view(), name="project_module"),
    path("module_list/", ProjectModuleListView.as_view(), name="module_list"),
    path("update_module/<int:pk>/",ProjectModuleUpdateView.as_view(), name="update_module"),
    path("delete_module/<int:pk>", ProjectModuleDeleteView.as_view(), name="delete_module"),
    path("create_task/", ProjectTaskCreateView.as_view(), name="create_task"),
    path("task_list/", ProjectTaskListView.as_view(), name="tasklist"),
    path("update_task/<int:pk>", ProjectTaskUpdateView.as_view(), name="update_task"),
    path("delete_task/<int:pk>", ProjectTaskDeleteView.as_view(), name="deletetask")

]
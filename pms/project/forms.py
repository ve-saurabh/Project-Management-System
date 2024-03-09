from django import forms
from .models import Project, ProjectTeam, ProjectModule, Task, UserTask


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'


class ProjectTeamCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields ='__all__'

class ProjectModuleCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'

class ProjectTaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


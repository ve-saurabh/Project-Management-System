from django.contrib import admin
from .models import Project, ProjectTeam, ProjectModule, Task, UserTask
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTeam)
admin.site.register(ProjectModule)
admin.site.register(Task)
admin.site.register(UserTask)

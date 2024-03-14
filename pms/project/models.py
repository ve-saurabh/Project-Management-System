from django.db import models
from user.models import User
# Create your models here.
techChoices  = (
    ('python','python'),
    ('Java','Java'),
    ('C++','C++'),
    ('C#','C#'),
)
class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    technology = models.CharField(max_length = 100, choices = techChoices)
    estimated_hours = models.PositiveBigIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()

    class Meta:
        db_table = "project"

    def __str__(self) -> str:
        return self.name


class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        db_table = "projectteam"

    def __str__(self) -> str:
        return self.user.username

statusChoices = (
    ('Not Started','Not Started'),
    ('In Progress','In Progress'),
    ('Completed','Completed')
)
class ProjectModule(models.Model):
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    moduleName = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    estimated_hours = models.PositiveBigIntegerField()
    status = models.CharField(choices = statusChoices, max_length = 100)
    startDate = models.DateField(null = True, blank = True)
    
    class Meta:
        db_table = "project_module"

    def __str__(self):
        return self.moduleName
    
#models.CASCADE means that when the referenced object is deleted, also delete the objects that have a foreign key pointing to it

priorityChoices = (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low')
)

taskSatatus = (
    ("Not Started","Not Started"),
    ("In Progress","In Progress"),
    ("Completed","Completed"),
)
class Task(models.Model):
    module = models.ForeignKey(ProjectModule, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    priority = models.CharField(choices = priorityChoices, max_length = 100)
    status = models.CharField(choices = taskSatatus, max_length = 100, default = False)
    description = models.CharField()
    hours = models.PositiveIntegerField(default = False)
    is_assigned = models.BooleanField(default = False, null = True, blank = True)

    class Meta:
        db_table = "task"

    def __str__(self):
        return self.title

class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add = True, null = True, blank = True)
    updated_at = models.DateField(auto_now = True, null = True, blank = True)  

    class Meta:
        db_table = "user_task"

    def __str__(self) -> str:
        return self.task.title +" - "+self.user.username


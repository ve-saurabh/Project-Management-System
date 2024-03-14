from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)
    salary = models.PositiveIntegerField(null = True, blank = True)
    first_name = models.CharField(max_length = 100, null= True)
    last_name = models.CharField(max_length = 100, null= True)
    address = models.CharField(max_length = 500, null= True)
    city = models.CharField(max_length = 100, null= True)
    country = models.CharField(max_length = 100, null= True)
    pincode = models.PositiveIntegerField(null = True)
    is_manager = models.BooleanField(default = False)
    is_developer = models.BooleanField(default = False)

    class Meta:
        db_table = "user"
        
    def __str__(self):
        return self.username
    
    
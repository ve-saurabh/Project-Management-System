from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction
from django.forms.models import ModelForm

class ManagerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'age', 'salary','password1', 'password2']
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user



class DeveloperRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'age', 'salary','password1', 'password2']
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_developer = True
        user.save()
        return user    
    
class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'address', 'city', 'country', 'pincode']

        
            
    
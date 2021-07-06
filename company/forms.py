from .models import MyUser,Employer,Job,Jobseeker
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["first_name","last_name","email","phone","gender","role","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class EmployerForm(forms.ModelForm):
    class Meta:
        model=Employer
        fields="__all__"

# class JobCreateForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = "__all__"


class JobCreateForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=["location","description","skills_req","salary","exp_req","job_status","closing_date"]

# class JobCreateForm(forms.Form):
#     employer=forms.ModelMultipleChoiceField(queryset=MyUser.objects.filter(role="Employer"))
#     location = forms.CharField()
#     description = forms.CharField()
#     skills_req = forms.CharField()
#     salary = forms.FloatField()
#     exp_req = forms.CharField()
#     job_options = (("Active", "Active"),
#                    ("Closed", "Closed"))
#     job_status = forms.CharField(widget=forms.Select(choices=job_options))
#     closing_date = forms.DateField()

class JobseekerProfileCreateForm(forms.ModelForm):
    class Meta:
        model=Jobseeker
        fields=["qualification","passout_year","skills","experience"]
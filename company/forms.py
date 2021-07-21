from .models import MyUser,Employer,Job,Jobseeker,Applications
from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from django.db import models

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["first_name","last_name","email","phone","gender","role","username","password1","password2"]
        widgets={
        "first_name": forms.TextInput(attrs={"class": "form-control form-label"}),
        "last_name": forms.TextInput(attrs={"class": "form-control form-label"}),
        "email": forms.TextInput(attrs={"class": "form-control form-label"}),
        "phone": forms.TextInput(attrs={"class": "form-control form-label"}),
        "username": forms.TextInput(attrs={"class": "form-control form-label"}),
        "password1": forms.PasswordInput(attrs={"class": "form-control form-label"}),
        "password2": forms.PasswordInput(attrs={"class": "form-control form-label"}),
       }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-label","placeholder":"Enter Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control form-label","placeholder":"Enter Username"}))

class EmployerForm(forms.ModelForm):
    class Meta:
        model=Employer
        fields=["location","website","address"]
        widgets = {
            "location": forms.TextInput(attrs={"class": "form-control form-label"}),
            "website": forms.TextInput(attrs={"class": "form-control form-label"}),
            "address": forms.Textarea(attrs={"class": "form-control form-label"})
        }

# class JobCreateForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = "__all__"


class JobCreateForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=["location","description","skills_req","salary","exp_req","job_status","closing_date"]
        widgets = {
            "location": forms.TextInput(attrs={"class": "form-control form-label"}),
            "description": forms.Textarea(attrs={"class": "form-control form-label"}),
            "skills_req": forms.Textarea(attrs={"class": "form-control form-label"}),
            "salary": forms.TextInput(attrs={"class": "form-control form-label"}),
            "exp_req": forms.TextInput(attrs={"class": "form-control form-label"}),
            "closing_date": forms.TextInput(attrs={"class": "form-control form-label"}),
        }
    def clean(self):
        cleaned_data=super().clean()
        closing_date=cleaned_data.get("closing_date")
        today=date.today()
        if closing_date<today:
            msg="invalid date"
            self.add_error("closing_date",msg)


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
        widgets = {
            "qualification": forms.TextInput(attrs={"class": "form-control form-label"}),
            "passout_year": forms.TextInput(attrs={"class": "form-control form-label"}),
            "skills": forms.Textarea(attrs={"class": "form-control form-label"}),
            "experience": forms.TextInput(attrs={"class": "form-control form-label"}),

        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model=Applications
        fields=["appllicant","application_status"]

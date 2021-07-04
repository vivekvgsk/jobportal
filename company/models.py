from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    phone=models.CharField(max_length=15)
    gender_options=(("Male","Male"),
             ("Female","Female"),
             ("Others","Others"))
    gender=models.CharField(max_length=10,choices=gender_options,default="Male")
    role_options=(("Employer","Employer"),
                  ("Jobseeker","Jobseeker"))
    role=models.CharField(max_length=15,choices=role_options,default="Jobseeker")

class Jobseeker(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    qualification=models.CharField(max_length=50)
    passout_year=models.IntegerField()
    skills=models.CharField(max_length=200)
    experience=models.CharField(max_length=100)

class Employer(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    website=models.URLField(max_length=50)
    address=models.CharField(max_length=100)

class Job(models.Model):
    employer=models.ForeignKey(Employer,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    location=models.CharField(max_length=20)
    description=models.CharField(max_length=250)
    skills_req=models.CharField(max_length=100)
    salary=models.FloatField()
    exp_req=models.CharField(max_length=10)
    date_posted=models.DateField(auto_now=True)
    closing_date=models.DateField()
    job_options=(("Active","Active"),
                 ("Closed","Closed"))
    job_status=models.CharField(max_length=10,choices=job_options,default="Active")

class Applications(models.Model):

    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    appllicant=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    applied_date=models.DateField(auto_now=True)
    app_options=(("Approved","Approved"),
                 ("Rejected","Rejected"),
                 ("Pending","Pending"))
    application_status=models.CharField(max_length=15,choices=app_options,default="Pending")



from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from company.models import MyUser,Job,Applications,Jobseeker
from company.forms import LoginForm,JobseekerProfileCreateForm
from django.contrib.auth import authenticate,login,logout
from company.views import AccountCreationView
from django.contrib import messages

# Create your views here.
class LoginView(TemplateView):
    model=MyUser
    form_class=LoginForm
    template_name = "jlogin.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        context={}
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                if user.role=="Jobseeker":
                    login(request,user)
                    return redirect("alljobs")
                else:
                    print("failed")
                    return redirect("register")

        return render(request, self.template_name, self.context)

class LogOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")


class JobListView(ListView):
    model=Job
    template_name="listjobs.html"
    context_object_name = "jobs"

class JobDetailView(DetailView):
    model=Job
    template_name="jobdetails.html"
    context_object_name ="job"

# class ApplyJob(TemplateView):
#
#     def post(self,request,*args,**kwargs):
#         jid=kwargs.get("id")
#         job=Job.objects.get(id=jid)
#         application=Applications(job=job,applicant=request.user)
#         application.save()
#         return redirect("alljobs")

def apply_job(request,*args,**kwargs):
    jid = kwargs.get("id")
    job = Job.objects.get(id=jid)
    application = Applications(job=job, appllicant=request.user)
    application.save()
    return redirect("alljobs")

class ListAppliedJobs(TemplateView):
    model=Applications
    template_name="applicationlist.html"
    context={}
    def get(self,request,*args,**kwargs):
        applications=self.model.objects.filter(appllicant_id=request.user.id)
        self.context["applications"]=applications
        return render(request,self.template_name,self.context)

class JobseekerProfileCreateView(TemplateView):
    model=Jobseeker
    form_class=JobseekerProfileCreateForm
    template_name="jprofilecreate.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            qualification=form.cleaned_data.get("qualification")
            passout_year=form.cleaned_data.get("passout_year")
            skills=form.cleaned_data.get("skills")
            experience=form.cleaned_data.get("experience")
            jobseeker=Jobseeker(user=request.user,qualification=qualification,passout_year=passout_year,skills=skills,experience=experience)
            try:
                jobseeker.save()
            except:
                messages.success(request,"you have already created your profile")
                return render(request, self.template_name, self.context)








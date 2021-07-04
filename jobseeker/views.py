from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from company.models import MyUser,Job,Applications
from company.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from company.views import AccountCreationView

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
                login(request,user)
                return redirect("home")
            else:
                print("failed")
                return redirect("register")

        return render(request, self.template_name, self.context)
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






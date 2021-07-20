from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import MyUser,Employer,Job,Applications
from .forms import UserRegistrationForm,LoginForm,EmployerForm,JobCreateForm,JobApplicationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import loginrequired
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
# Create your views here.
# Registration view
class AccountCreationView(CreateView):
    model=MyUser
    form_class = UserRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("signin")
#Login

class SignInView(TemplateView):
    model=MyUser
    form_class=LoginForm
    template_name="login.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                if user.role=="Employer":
                    login(request,user)

                    return redirect("postedjobs")

                else:
                    messages.error(request,"Invalid User")
                    return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)

class SignOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

@method_decorator(loginrequired,name="dispatch")
class EmployerCreateView(CreateView):
    model=Employer
    form_class = EmployerForm
    template_name="addemployerdetails.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            location=form.cleaned_data.get("location")
            website=form.cleaned_data.get("website")
            address=form.cleaned_data.get("address")
            employer=Employer(user=request.user,location=location,website=website,address=address)
            try:
                employer.save()
            except:
                messages.error(request,"you have already created your profile")
            return render(request, self.template_name, self.context)

class EmployerProfileDispalyView(TemplateView):
    model=Employer
    template_name = "employerprofile.html"
    context={}

    def get(self, request, *args, **kwargs):
        employer = self.model.objects.filter(user=request.user)
        self.context["employer"] =employer
        return render(request, self.template_name, self.context)
# class JobCreateView(CreateView):
#     model=Job
#     form_class = JobCreateForm
#     template_name = "createjob.html"
#     success_url = reverse_lazy("postedjobs")

# class JobCreateView(TemplateView):
#     model= Job
#     form_class=JobCreateForm
#     template_name = "createjob.html"
#     context={}
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         self.context["form"] = form
#         return render(request, self.template_name, self.context)
#     def post(self,request,*args,**kwargs):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             user=form.cleaned_data.get("user")
#             if user==request.user:
#                 form.save()
#                 return redirect("postedjobs")
#             else:
#                 print("please check your company name")
#
#
#
#
#
#
#         return render(request, self.template_name, self.context)
#





# class ListPostedJobView(ListView):
#     model=Job
#     context_object_name = "jobs"
#     template_name = "listpostedjobs.html"
@method_decorator(loginrequired,name="dispatch")
class ListPostedJobView(TemplateView):
    model=Job
    context={}
    template_name = "listpostedjobs.html"
    def get(self,request,*args,**kwargs):
        jobs=Job.objects.filter(user=request.user).order_by("date_posted")
        self.context["jobs"]=jobs
        return render(request, self.template_name, self.context)






@method_decorator(loginrequired,name="dispatch")
class EditJobView(UpdateView):
    model=Job
    form_class = JobCreateForm
    template_name = "editjob.html"
    success_url = reverse_lazy("postedjobs")

@method_decorator(loginrequired,name="dispatch")
class JobDeleteView(DeleteView):
    model=Job
    template_name = "deletejob.html"
    success_url = reverse_lazy("postedjobs")

@method_decorator(loginrequired,name="dispatch")
class ApplicantListView(TemplateView):
    model=Applications
    context={}
    template_name = "applicantlist.html"
    def get(self,request,*args,**kwargs):


        applications=self.model.objects.filter(job__employer__user__first_name=request.user)
        self.context["applications"]=applications
        return render(request, self.template_name, self.context)

@method_decorator(loginrequired,name="dispatch")
class JobCreateView(TemplateView):
    model= Job
    form_class=JobCreateForm
    template_name = "createjob.html"
    context={}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            location=form.cleaned_data.get("location")
            description=form.cleaned_data.get("description")
            skills_req=form.cleaned_data.get("skills_req")
            salary=form.cleaned_data.get("salary")
            exp_req=form.cleaned_data.get("exp_req")
            job_status=form.cleaned_data.get("job_status")
            closing_date=form.cleaned_data.get("closing_date")
            job=Job(employer_id=request.user.id,user=request.user,location=location,description=description,
                    skills_req=skills_req,salary=salary,exp_req=exp_req,job_status=job_status,closing_date=closing_date)
            job.save()
        return render(request, self.template_name, self.context)

# class GetObjectMixin:
#     def get_obect(self,id):
#         return self.model.objects.get(id=id)

# @method_decorator(loginrequired,name="dispatch")
# class UpdateApplicationStatusView(UpdateView):
#     model=Applications
#     form_class=JobApplicationForm
#     template_name = "applicationstatus.html"
#     success_url = reverse_lazy("applicants")

@method_decorator(loginrequired,name="dispatch")
class UpdateApplicationStatusView(TemplateView):
    model=Applications
    form_class=JobApplicationForm
    template_name = "applicationstatus.html"
    context={}
    def get(self,request,*args,**kwargs):
        aid = kwargs.get("id")
        application = self.model.objects.get(id=aid)
        form=self.form_class(instance=application)
        self.context["form"]=form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        aid = kwargs.get("id")
        application = self.model.objects.get(id=aid)
        form=self.form_class(instance=application,data=request.POST)
        if form.is_valid():
            form.save()
            applicant=form.cleaned_data.get("appllicant")
            status=form.cleaned_data.get("application_status")
            email=applicant.email
            print(email)
            # jid=Applications.job.job_id
            # application=self.model(job_id=jid,appllicant=applicant,application_status=status)
            # application.save()


            msg="Dear Candidate, " \
                "Your Application has been   "+status+"  by the employer SELECTED Candidates may please contact our HR department for further informations"
            send_mail(
                'Reply for your Job Application',
                msg,
                'vivekvgsk@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect("applicants")
        return render(request, self.template_name, self.context)



















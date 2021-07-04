from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import MyUser,Employer,Job,Applications
from .forms import UserRegistrationForm,LoginForm,EmployerForm,JobCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
                login(request,user)
                return redirect("postedjobs")
            else:
                print("failed")
        return render(request, self.template_name, self.context)

class SignOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


class EmployerCreateView(CreateView):
    model=Employer
    form_class = EmployerForm
    template_name="addemployerdetails.html"
    success_url=reverse_lazy("addjob")

# class JobCreateView(CreateView):
#     model=Job
#     form_class = JobCreateForm
#     template_name = "createjob.html"
#     success_url = reverse_lazy("postedjobs")

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
            user=form.cleaned_data.get("user")
            if user==request.user:
                form.save()
                return redirect("postedjobs")
            else:
                print("please check your company name")






        return render(request, self.template_name, self.context)






# class ListPostedJobView(ListView):
#     model=Job
#     context_object_name = "jobs"
#     template_name = "listpostedjobs.html"

class ListPostedJobView(TemplateView):
    model=Job
    context={}
    template_name = "listpostedjobs.html"
    def get(self,request,*args,**kwargs):
        jobs=Job.objects.filter(user=request.user)
        self.context["jobs"]=jobs
        return render(request, self.template_name, self.context)







class EditJobView(UpdateView):
    model=Job
    form_class = JobCreateForm
    template_name = "editjob.html"
    success_url = reverse_lazy("postedjobs")

class JobDeleteView(DeleteView):
    model=Job
    template_name = "deletejob.html"
    success_url = reverse_lazy("postedjobs")


class ApplicantListView(TemplateView):
    model=Applications
    context={}
    template_name = "applicantlist.html"
    def get(self,request,*args,**kwargs):

        applications=self.model.objects.filter(job=request.user)
        self.context["applications"]=applications
        return render(request, self.template_name, self.context)






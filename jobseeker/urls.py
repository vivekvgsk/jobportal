from django.urls import path
from django.views.generic import TemplateView
from .views import LoginView
from company.views import AccountCreationView,SignInView
from .views import JobListView,JobDetailView,apply_job,ListAppliedJobs,JobseekerProfileCreateView,LogOutView,JobFilterView

urlpatterns = [
    path("login",LoginView.as_view(),name="login"),
    path("signin", SignInView.as_view(), name="signin"),
    path("register",AccountCreationView.as_view(),name="register"),
    path("home",TemplateView.as_view(template_name="jhome.html"),name="home"),
    path("jobs",JobListView.as_view(),name="alljobs"),
    path("job/<int:pk>",JobDetailView.as_view(),name="jobdetail"),

    path("apply/<int:id>",apply_job,name="apply"),
    path("appliedjobs",ListAppliedJobs.as_view(),name="listappliedjobs"),
    path("profile",JobseekerProfileCreateView.as_view(),name="jprofile"),
    path("logout",LogOutView.as_view(),name="logout"),
    path("filter",JobFilterView.as_view(),name="filter"),
    # path("profiledisplay/<int:pk>",JobseekerProfileDispaly.as_view(),name="jprofiledispaly")



]
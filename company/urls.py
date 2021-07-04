from django.views.generic import TemplateView
from django.urls import path
from .views import AccountCreationView,SignInView,EmployerCreateView,JobCreateView,ListPostedJobView,EditJobView,JobDeleteView,SignOutView,ApplicantListView

urlpatterns = [
   path("register",AccountCreationView.as_view(),name="register"),
    path("login",SignInView.as_view(),name="signin"),
    path("logout",SignOutView.as_view(),name="signout"),
    path("home",TemplateView.as_view(template_name="userhome.html"),name="userhome"),
    path("empprofile",EmployerCreateView.as_view(),name="employerprofile"),
    path("addjob",JobCreateView.as_view(),name="addjob"),
    path("postedjobs",ListPostedJobView.as_view(),name="postedjobs"),
    path("editjob/<int:pk>",EditJobView.as_view(),name="update"),
    path("removejob/<int:pk>",JobDeleteView.as_view(),name="removejob"),
 path("applicants",ApplicantListView.as_view(),name="applicants")


]
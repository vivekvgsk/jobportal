from django.views.generic import TemplateView
from django.urls import path
from .views import AccountCreationView,SignInView,EmployerCreateView,JobCreateView,ListPostedJobView,EditJobView,JobDeleteView,SignOutView,ApplicantListView,EmployerProfileDispalyView,UpdateApplicationStatusView,EmployerProfileEditView,ApplicantProfileView

urlpatterns = [
   path("register",AccountCreationView.as_view(),name="register"),
    path("login",SignInView.as_view(),name="signin"),
    path("logout",SignOutView.as_view(),name="signout"),
    path("home",TemplateView.as_view(template_name="userhome.html"),name="userhome"),
    path("empprofile",EmployerCreateView.as_view(),name="employerprofile"),
    path("empprofiledisplay",EmployerProfileDispalyView.as_view(),name="empprofileview"),
    path("empprofileedit/<int:pk>",EmployerProfileEditView.as_view(),name="empprofileedit"),
    path("addjob",JobCreateView.as_view(),name="addjob"),
    path("postedjobs",ListPostedJobView.as_view(),name="postedjobs"),
    path("editjob/<int:pk>",EditJobView.as_view(),name="update"),
    path("removejob/<int:pk>",JobDeleteView.as_view(),name="removejob"),
    path("applicants",ApplicantListView.as_view(),name="applicants"),
    path("status/<int:id>",UpdateApplicationStatusView.as_view(),name="updatestatus"),
    path("applicantprofile/<int:pk>",ApplicantProfileView.as_view(),name="applicantprofile")



]
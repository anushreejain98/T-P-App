from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
app_name='tpcm_app'

from . import views
from .forms import StudentLoginForm, CompanyLoginForm
urlpatterns = [
    
    #/tpcm_app/
    #url(r'^$',views.detail,name='detail'),
    #url(r'student/$',views.stud,name='stud'),
    #url(r'company/$',views.cmp,name='cmp'),
    path('', views.detail, name='home'),
    path('login/type/', views.login_type, name='logintype'),
    path('signup/type/', views.signup_type, name='signuptype'),
    path('signup/student/', views.StudentSignUpView.as_view(), name='stud'),
    path('signup/company', views.CompanySignUpView.as_view(), name='cmp'),
    path('login/student', auth_views.LoginView.as_view(template_name="login/studentlogin.html"
    , authentication_form=StudentLoginForm), name='slogin'),
    path('login/company', auth_views.LoginView.as_view(template_name="login/companylogin.html"
    , authentication_form=CompanyLoginForm), name='clogin'),
    path('signout/', auth_views.LogoutView.as_view(template_name="home.html"), name='signout'),
    path('student/profile/update', views.student_update_profile, name='student_update'),
    path('student/profile', views.student_profile, name='student_profile'),
    path('company/createjob',views.CreatePositionView.as_view(),name='cmp_createjob'),
]
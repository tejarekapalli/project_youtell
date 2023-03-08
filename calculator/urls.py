from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('master/signup/', master_signup, name='master_signup'),
    path('student/signup/', student_signup, name='student_signup'),
    path('master/activity-log/', master_activity_log, name='master_activity_log'),
    path('master/process-calculation/<int:calculation_id>/', master_process_calculation, name='master_process_calculation'),
    path('student/submit-calculation/', student_submit_calculation, name='student_submit_calculation'),
    path('student/activity-log/', student_activity_log, name='student_activity_log'),
]


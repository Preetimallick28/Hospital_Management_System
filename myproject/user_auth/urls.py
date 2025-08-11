from django.urls import path
from user_auth import views

urlpatterns = [
    path('admin_login',views.admin_login_,name='admin_login'),
    path('admin_registration',views.admin_registration_,name='admin_registration'),
    path('doctor_login',views.doctor_login_,name='doctor_login'),
    path('doctor_registration',views.doctor_registration_,name='doctor_registration'),
    path('doctor_profile',views.doctor_profile,name='doctor_profile'),
    path('doctor_profile_update/<str:pk>',views.doctor_update_profile,name='doctor_update_profile'),
    path('doctor_profile_reset_pass',views.doctor_profile_reset_pass,name='doctor_profile_reset_pass'),
    path('logout_',views.logout_,name='logout'),
    path('admin_profile',views.admin_profile,name='admin_profile'),
    

]

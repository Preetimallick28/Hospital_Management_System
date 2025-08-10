from django.urls import path
from user_auth import views

urlpatterns = [
    path('admin_login',views.admin_login_,name='admin_login'),
    path('admin_registration',views.admin_registration_,name='admin_registration'),
    path('doctor_login',views.doctor_login_,name='doctor_login'),
    path('doctor_registration',views.doctor_registration_,name='doctor_registration'),
    

]

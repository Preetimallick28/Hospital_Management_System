from django.urls import path
from admin_dashboard import views

urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('add_appointment',views.add_appointment,name='add_appointment'),
    path('admin_view_patient',views.admin_view_patient,name='admin_view_patient'),
    path('admin_update_patient/<int:pk>',views.admin_update_patient,name='admin_update_patient'),
    path('admin_delete_patient/<int:pk>',views.admin_delete_patient,name='admin_delete_patient'),
    path('admin_view_appointment',views.admin_view_appointment,name='admin_view_appointment'),
    path('admin_update_appointment/<int:pk>',views.admin_update_appointment,name='admin_update_appointment'),
    path('admin_delete_appointment/<int:pk>',views.admin_delete_appointment,name='admin_delete_appointment'),
    path('doctor_list',views.doctors_list,name='doctor_list'),


]

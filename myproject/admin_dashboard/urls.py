from django.urls import path
from admin_dashboard import views

urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('add_appointment',views.add_appointment,name='add_appointment'),
    path('view_patient',views.view_patient,name='view_patient'),
    path('update_patient',views.update_patient,name='update_patient'),
    path('delete_patient',views.delete_patient,name='delete_patient'),
    path('view_appointment',views.view_appointment,name='view_appointment'),
    path('update_appointment',views.update_appointment,name='update_appointment'),
    path('delete_appointment',views.delete_appointment,name='delete_appointment'),


]

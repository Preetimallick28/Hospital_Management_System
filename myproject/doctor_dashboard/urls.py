from django.urls import path
from doctor_dashboard import views

urlpatterns = [
    path('doctor_home',views.doctor_home,name='doctor_home'),
    path('doctor_view_patient',views.doctor_view_patient,name='doctor_view_patient'),
    path('doctor_view_appointment',views.doctor_view_appointment,name='doctor_view_appointment'),
    path('doctor_view_appointment',views.doctor_view_appointment,name='doctor_view_appointment'),
    path('doctor_patient_update/<int:pk>',views.doctor_patient_update,name='doctor_patient_update'),
    path('doctor_appointment_update/<int:pk>',views.doctor_appointment_update,name='doctor_appointment_update'),
    path('doctor_delete_appointment/<int:pk>',views.doctor_delete_appointment,name='doctor_delete_appointment'),
]

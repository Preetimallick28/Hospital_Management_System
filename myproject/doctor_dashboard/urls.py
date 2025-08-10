from django.urls import path
from doctor_dashboard import views

urlpatterns = [
    path('doctor_home',views.doctor_home,name='doctor_home')
]

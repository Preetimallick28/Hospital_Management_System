from django.shortcuts import render,redirect


# Create your views here.
def admin_home(request):
    return render(request,'admin_home.html')

def add_patient(request):
    return render(request,'add_patient.html')

def add_appointment(request):
    return render(request,'add_appointment.html')

def view_patient(request):
    return render(request,'view_patient.html')

def update_patient(request):
    return render(request,'update_patient.html')

def delete_patient(request):
    return render(request,'delete_patient.html')

def view_appointment(request):
    return render(request,'view_appointment.html')

def update_appointment(request):
    return render(request,'update_appointment.html')

def delete_appointment(request):
    return render(request,'delete_appointment.html')


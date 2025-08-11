from django.shortcuts import render,redirect
from doctor_dashboard.models import Patient
from admin_dashboard.models import Appointment
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def doctor_home(request):

    return render(request,'doctor_home.html')

def doctor_view_patient(request):
    patients = Patient.objects.filter(doctor_id=request.user.id)
    return render(request,'doctor_view_patient.html',{'patient':patients})


def doctor_view_appointment(request):
    appointment = Appointment.objects.filter(doctor_id=request.user.id)
    return render(request,'view_appointment.html',{'appointment':appointment})

def doctor_patient_update(request,pk):
    u = Patient.objects.get(id=pk)
    doctors = User.objects.all()
    if request.method == 'POST':
        patient_name = request.POST['name']
        doctor_id = request.POST['doctor']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']

        u.name = patient_name
        u.doctor = User.objects.get(id=doctor_id)
        u.age = age
        u.gender = gender
        u.contact_number = phone
        u.address = address
        u.save()

        return redirect('doctor_view_patient')
    return render(request,'doctor_patient_update.html',{'u':u,'doctors':doctors})

def doctor_appointment_update(request,pk):
    u = Appointment.objects.get(id=pk)

    if request.method == 'POST':
        patient_id = request.POST['patient']
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST['reason']

        u.patient = Patient.objects.get(id=patient_id)
        u.doctor = User.objects.get(id=doctor_id)
        u.date = date
        u.time = time
        u.reason = reason
        u.save()

        return redirect('doctor_view_appointment')

    patients = Patient.objects.all()
    doctors = User.objects.all()
    return render(request,'doctor_appointment_update.html',{'u': u,'patients': patients,'doctors': doctors})
    
def doctor_delete_appointment(request,pk):
    delete_data = Appointment.objects.get(id=pk)
    delete_data.delete()
    return redirect('doctor_view_appointment')
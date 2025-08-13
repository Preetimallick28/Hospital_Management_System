from django.shortcuts import render,redirect
from doctor_dashboard.models import Patient
from admin_dashboard.models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='doctor_login')
def doctor_home(request):
    patient_count = Patient.objects.filter(doctor=request.user).count()
    appointment_count = Appointment.objects.filter(doctor=request.user).count()

    context = {
        'patient_count': patient_count,
        'appointment_count': appointment_count,
    }
    return render(request,'doctor_home.html',context)

@login_required
def doctor_view_patient(request):
    
    if request.method=='GET':
        if 'q' in request.GET:
            q_data = request.GET['q']
            print(q_data)
            data = Patient.objects.filter(Q(name__icontains=q_data))
        else:
            data=Patient.objects.filter(doctor=request.user)
    return render(request,'doctor_view_patient.html',{'patient':data})

@login_required
def doctor_view_appointment(request):
    if request.method=='GET':
        if 'q' in request.GET:
            q_data = request.GET['q']
            print(q_data)
            data = Appointment.objects.filter(Q(patient__name__icontains=q_data))
        else:
            data=Appointment.objects.filter()
    return render(request,'doctor_view_appointment.html',{'appointment':data})
@login_required
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
@login_required
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
@login_required    
def doctor_delete_appointment(request,pk):
    delete_data = Appointment.objects.get(id=pk)
    delete_data.delete()
    return redirect('doctor_view_appointment')
@login_required
def doctor_patient_delete(request,pk):
    delete_data = Patient.objects.get(id=pk)
    delete_data.delete()
    return redirect('doctor_view_appointment')
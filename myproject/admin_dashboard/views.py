from django.shortcuts import render,redirect
from doctor_dashboard.models import Patient
from admin_dashboard.models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required(login_url='admin_login')
def admin_home(request):
    patient_count = Patient.objects.count()
    doctor_count = User.objects.filter(is_staff=False).count()
    appointment_count = Appointment.objects.count()

    context = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'appointment_count': appointment_count,
    }
    return render(request,'admin_home.html',context)

@login_required
def doctors_list(request):
    list = User.objects.filter(is_staff=False)
    return render(request,'doctor_list.html',{'list':list})


@login_required
def add_patient(request):
    doctor_list = User.objects.filter(is_staff=False)
    
    if request.method=='POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        doctor_id = request.POST['doctor']  
        doctor = User.objects.get(id=doctor_id)  

        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            contact_number = phone,
            address=address,
            doctor=doctor
        )
        return redirect('admin_view_patient')
        
    return render(request,'add_patient.html',{'doctors':doctor_list})


@login_required
def add_appointment(request):
    if request.method=='POST':
        patient_id = request.POST['patient']  # Comes as a string
        patient = Patient.objects.get(id=patient_id)
        doctor_id = request.POST['doctor']  
        doctor = User.objects.get(id=doctor_id)
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST['reason']
          

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time = time,
            reason=reason,
            
        )
        return redirect('admin_view_appointment')
    doctor_list = User.objects.filter(is_staff=False)
    patient = Patient.objects.all()
    return render(request,'add_appointment.html',{'doctors':doctor_list,'patient':patient})

@login_required
def admin_view_patient(request):
    if request.method=='GET':
        if 'q' in request.GET:
            q_data = request.GET['q']
            print(q_data)
            data = Patient.objects.filter(Q(name__icontains=q_data))
        else:
            data=Patient.objects.all()
    return render(request,'view_patient.html',{'data':data})

@login_required
def admin_update_patient(request,pk):
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

        return redirect('admin_view_patient')
    return render(request,'update_patient.html',{'u':u,'doctors':doctors})

@login_required
def admin_delete_patient(request,pk):
    delete_data = Patient.objects.get(id=pk)
    delete_data.delete()
    return redirect('admin_view_patient')

@login_required
def admin_view_appointment(request):
    if request.method=='GET':
        if 'q' in request.GET:
            q_data = request.GET['q']
            print(q_data)
            data = Appointment.objects.filter(Q(patient__name__icontains=q_data))
        else:
            data=Appointment.objects.all()
    return render(request,'view_appointment.html',{'search':data})


@login_required
def admin_update_appointment(request,pk):
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

        return redirect('admin_view_appointment')

    patients = Patient.objects.all()
    doctors = User.objects.all()
    return render(request, 'update_appointment.html', {'u': u,'patients': patients,'doctors': doctors})


@login_required
def admin_delete_appointment(request,pk):
    delete_data = Appointment.objects.get(id=pk)
    delete_data.delete()
    return redirect('admin_view_appointment')


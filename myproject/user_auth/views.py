from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout

# Create your views here.
def admin_registration_(request):
    context={}
    if request.method=='POST':
        firstname = request.POST['admin_fname']
        lastname = request.POST['admin_lname']
        email = request.POST['email']
        is_staff = request.POST['is_staff']
        username = request.POST['username']
        password = request.POST['password']
        u = User.objects.all()
        for users in u:
            if users.username == username:
                context['error'] = 'username already exist! choose another username'
                return render(request,'admin_registration.html',context)

        u=User.objects.create(
            first_name = firstname,
            last_name = lastname,
            email = email,
            username = username,
            is_staff = True if is_staff == "yes" else False

        )
        # set_password() used to store password in encrypted format
        u.set_password(password)
        u.save()
        return redirect('admin_login')
    #IntegrityError - unique constraint failed:auth_username -  when same username is used
        
    return render(request,'admin_registration.html')

def admin_login_(request):
    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        # print(username_data,password_data)
        u=authenticate(username=username_data , password = password_data) #return boolean value
        print(u)
        # if credential is matching it will return user_out(true) and if not matching return None
        if u is not None:
            login(request,u)
            return redirect('admin_home')
        else:
            return render(request,'login.html',{'wrong_':True})
        
    return render(request,'admin_login.html') 

def doctor_registration_(request):
    return render(request,'doctor_registration.html')

def doctor_login_(request):
    return render(request,'doctor_login.html')


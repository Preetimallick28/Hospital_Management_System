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
            return render(request,'admin_login.html',{'wrong_':True})
        
    return render(request,'admin_login.html') 

def admin_profile(request):
    return render(request,'admin_profile.html')

def admin_update_profile(request,pk):
    profile_data = User.objects.get(username=pk)
    u=User.objects.get(username=pk)
    if request.method=='POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']

        u.first_name = first_name
        u.last_name = last_name
        u.email = email
        u.username = username
        u.save()
        return redirect('admin_profile')
    return render(request,'admin_update_profile.html',{'u':profile_data})

def admin_reset_pass(request):
    context={}
    user_record = User.objects.get(username=request.user)
    print(user_record.password)
    if request.method=='POST':
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        
        u= authenticate(username=user_record.username , password=old_pass)
        # print(old_pass,new_pass)
        if u is not None:
            user_record.set_password(new_pass)
            user_record.save()
            logout(request)
            return redirect('admin_login')
        else:
            context['error']='you have entered wrong old password'
            return render(request,'admin_reset_pass.html',context)
        
    return render(request,'admin_reset_pass.html')

def doctor_registration_(request):
    context={}
    if request.method=='POST':
        firstname = request.POST['doctor_fname']
        lastname = request.POST['doctor_lname']
        email = request.POST['email']
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

        )
        # set_password() used to store password in encrypted format
        u.set_password(password)
        u.save()
        return redirect('doctor_login')
    return render(request,'doctor_registration.html')

def doctor_login_(request):
    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        # print(username_data,password_data)
        u=authenticate(username=username_data , password = password_data) #return boolean value
        print(u)
        # if credential is matching it will return user_out(true) and if not matching return None
        if u is not None:
            login(request,u)
            return redirect('doctor_home')
        else:
            return render(request,'doctor_login.html',{'wrong_':True})
    return render(request,'doctor_login.html')

def doctor_profile(request):
    return render(request,'doctor_profile.html')

def doctor_profile_reset_pass(request):
    context={}
    user_record = User.objects.get(username=request.user)
    print(user_record.password)
    if request.method=='POST':
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        
        u= authenticate(username=user_record.username , password=old_pass)
        # print(old_pass,new_pass)
        if u is not None:
            user_record.set_password(new_pass)
            user_record.save()
            logout(request)
            return redirect('doctor_login')
        else:
            context['error']='you have entered wrong old password'
            return render(request,'doctor_profile_reset_pass.html',context)
        
    return render(request,'doctor_profile_reset_pass.html')


def doctor_update_profile(request,pk):
    u=User.objects.get(username=pk)
    if request.method=='POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']

        u.first_name = first_name
        u.last_name = last_name
        u.email = email
        u.username = username
        u.save()
        return redirect('doctor_profile')
    return render(request,'doctor_profile_update.html',{'u':u})

def logout_(request):
    logout(request)
    return redirect('doctor_login')
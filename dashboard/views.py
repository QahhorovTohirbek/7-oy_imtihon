from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main import models


@login_required(login_url='dashboard:log_in')
def index(request):
    """ Admin panel bosh sahifasi """
    user = User.objects.count()
    users = User.objects.all()

    staff = models.Staff.objects.count()

    context = {
        'user':user,
        'users':users,
        'staff':staff
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='dashboard:log_in')
def edit_profile(request, id):
    """Edit user profile"""
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                pass
            else:
                user.set_password(new_password)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect('dashboard:index')
    return render(request, 'dashboard/profile.html', {'user': user})



#--------Staff section-----------
def create_staff(request):
    """ Xodim qo'shish """
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        models.Staff.objects.create(first_name=first_name, last_name=last_name)
    return render(request, 'dashboard/staff/create.html')


def list_staff(request):
    """ Xodimlar ro'yxati """
    staff = models.Staff.objects.all()
    context = {
        'staff':staff,
    }
    return render(request, 'dashboard/staff/list.html', context)


def update_staff(request, id):
    """ Xodimlarni tahrirlash """
    staff = models.Staff.objects.get(id=id)
    if request.method =='POST':
        staff.first_name=request.POST['first_name']
        staff.last_name=request.POST['last_name']
        staff.save()
        return redirect('dashboard:list_staff')
    return render(request, 'dashboard/staff/update.html')

        

def delete_staff(request, id):
    """ Xodimlarni o'chirish """
    models.Staff.objects.get(id=id).delete()
    return redirect('dashboard:list_staff')



#---------Atttendance-------------
def list_attendance(request):
    attendance = models.Attendance.objects.all()
    context = {
        'attendance':attendance,
    }
    return render(request, 'dashboard/attendance/list.html', context)





#----------Avtorizatsiya-----------
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
    return render(request, 'auth/login.html')


def log_out(request):
    logout(request)
    return redirect('dashboard:index')


   




from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from StudentApp.forms import LoginForm, CollegeAdminForm, StudentForm
from StudentApp.models import Student


# Create your views here.
# home view
def home_view(request):
    return render(request, 'index.html')


def admin_home(request):
    return render(request, 'admin/base/admin_home.html')


def stud_home(request):
    return render(request, 'student/base/stud_home.html')


def register_admin(request):
    log_form = LoginForm()
    admin_form = CollegeAdminForm()
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        admin_form = CollegeAdminForm(request.POST)
        if log_form.is_valid() and admin_form.is_valid():
            log1 = log_form.save(commit=False)
            log1.is_staff = True
            log1.save()
            admin1 = admin_form.save(commit=False)
            admin1.user = log1
            admin1.save()
            return redirect('mylogin')
    return render(request, 'admin_register.html', {'admin_form': admin_form, 'log_form': log_form})


# student registration view
def register_stud(request):
    log_form = LoginForm()
    stud_form = StudentForm()
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        stud_form = StudentForm(request.POST, request.FILES)
        if log_form.is_valid() and stud_form.is_valid():
            log1 = log_form.save(commit=False)
            log1.is_student = True
            log1.save()
            stud1 = stud_form.save(commit=False)
            stud1.user = log1
            stud1.save()
            return redirect('mylogin')
    return render(request, 'stud_register.html', {'stud_form': stud_form, 'log_form': log_form})


# login view
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_staff:
            return redirect('studlist')
        elif user.is_student:
            profile = Student.objects.get(user=user)
            request.session['photo_url'] = profile.photo.url
            return redirect('myprofile')
        else:
            messages.error(request, "Invalid Credentials!")
    return render(request, "login.html")


# log out view
def logout_view(request):
    request.session.clear()
    logout(request)
    return redirect('home')

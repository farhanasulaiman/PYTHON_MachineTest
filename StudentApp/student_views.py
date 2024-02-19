from datetime import date

from django.shortcuts import render, redirect

from StudentApp.forms import StudentForm
from StudentApp.models import Student


def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def view_profile(request):
    curr_user = Student.objects.get(user=request.user)
    curr_user.dob=calculate_age(curr_user.dob)
    return render(request, 'student/view_profile.html', {"data": curr_user})


def updt_profile(request):
    curr_user = Student.objects.get(user=request.user)
    stud_form = StudentForm(instance=curr_user)
    if request.method == "POST":
        stud_form1 = StudentForm(request.POST, request.FILES, instance=curr_user)
        if stud_form1.is_valid():
            stud_form1.save()
            return redirect('myprofile')
        else:
            stud_form = stud_form1
    return render(request, 'student/updt_profile.html', {"stud_form": stud_form})
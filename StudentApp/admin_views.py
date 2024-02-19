# view student list
from datetime import date

from django.shortcuts import render, redirect

from StudentApp.forms import StudentForm, MarksForm, UpdtMarksForm
from StudentApp.models import Student, Marks


def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def view_stud(request):
    data = Student.objects.filter().order_by('id')
    for student in data:
        student.dob = calculate_age(student.dob)
    return render(request, "admin/view_stud.html", {"data": data})


# update student record
def updt_stud(request, id):
    record = Student.objects.get(id=id)
    stud_form = StudentForm(instance=record)
    if request.method == "POST":
        stud_form1 = StudentForm(request.POST, request.FILES, instance=record)
        if stud_form1.is_valid():
            stud_form1.save()
            return redirect('studlist')
        else:
            stud_form = stud_form1
    return render(request, 'admin/updt_stud.html', {"stud_form": stud_form})


def add_marks(request):
    marks_form = MarksForm()
    if request.method == 'POST':
        marks_form1 = MarksForm(request.POST)
        if marks_form1.is_valid():
            marks_form1.save()
        else:
            marks_form = marks_form1
    return render(request, 'admin/add_marks.html', {"marks_form": marks_form})


def view_marks(request):
    mark_data = Marks.objects.filter().order_by('id')
    return render(request, "admin/view_marks.html", {"mark_data": mark_data})


def updt_marks(request, id):
    record = Marks.objects.get(id=id)
    mark_form = UpdtMarksForm(instance=record)
    if request.method == "POST":
        mark_form1 = UpdtMarksForm(request.POST, instance=record)
        if mark_form1.is_valid():
            mark_form1.save()
            return redirect('markslist')
        else:
            mark_form = mark_form1
    return render(request, 'admin/updt_marks.html', {"mark_form": mark_form})


def del_marks(request, id):
    if request.method == 'POST':
        record = Marks.objects.get(id=id)
        record.delete()
        return redirect('markslist')
    return render(request, 'admin/view_marks.html')


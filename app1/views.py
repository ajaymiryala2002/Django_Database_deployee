from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    context={"students": students}
    return render(request, "student_list.html",context)

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "student_form.html", {"form": form})


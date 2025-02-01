from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
        else:
            messages.error(request, "Failed to add student. Please check the form for errors.")
    else:
        form = StudentForm()

    context = {
        'form': form,
        'action': 'Add',  # Specify the action for template clarity
        'button_text': 'Add Student',  # Button text in the template
    }
    return render(request, 'students/student_form.html', context)  # Changed template name for reuse

# Update student details
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
        else:
            messages.error(request, "Failed to update student. Please check the form for errors.")
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'action': 'Update',  # Specify the action for template clarity
        'button_text': 'Update Student',  # Button text in the template
    }
    return render(request, 'students/student_form.html', context)  # Reusing template for adding and updating

# Delete a student
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')

    context = {
        'student': student,
    }
    return render(request, 'students/delete_student.html', context)

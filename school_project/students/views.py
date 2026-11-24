from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Student


def student_list(request):
    query = request.GET.get('q', '').strip()
    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    return render(request, 'students/student_list.html', {
        'students': students,
        'query': query,
    })


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/student_detail.html', {'student': student})


def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)
    return render(request, 'students/student_list.html', {
        'students': students,
        'query': '',
        'classe': classe,
    })
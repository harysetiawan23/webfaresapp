from django.shortcuts import render
from .models import studentClass as studentInClass


# Create your views here.

def studentClass(request):
    studentClassData = studentInClass.objects.all()
    studentClassDataCount = len(studentClassData)
    context = {
        'title': 'Kelas Pelajar',
        'breadcumbs': [
            ['/', 'Home'],
            ['/control/kelas-pelajar', 'Penawaran Mata Pelajaran']
        ],
        'data': studentClassData,
        'studentClassDataCount': studentClassDataCount
    }
    return render(request, 'scheduling-vew/master-student-class.html', context)


def scheduleClass(request):
    return render(request, 'scheduling-vew/master-schedule.html')

from django.shortcuts import render
from .models import studentClass as studentInClass
from master_jadwal.models import subject_offer, dtTeamTeaching
from master_user.models import FaresUser
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
class controlStudentClass():

    @login_required
    def scheduleClass(request):
        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        subjectOffer = subject_offer.objects.filter(subject_id__dept_id_id=userData.dept_id_id)
        subjectOfferCount = len(subjectOffer)
        context = {
            'title': 'Kelas Pelajar',
            'breadcumbs': [
                ['/', 'Manajemen'],
                ['/control/kelas-pelajar', 'Kelas']
            ],
            'data': subjectOffer,
            'studentClassDataCount': subjectOfferCount,
        }
        return render(request, 'scheduling-vew/master-schedule.html', context)

    @login_required
    def studentClass(request):
        if request.GET:
            userData = FaresUser.objects.get(pk=str(request.session['userId']))
            allStudent = FaresUser.objects.filter(dept_id_id=userData.dept_id_id).filter(isTeacher=False)
            studentClassData = studentInClass.objects.filter(subjectOfferId_id=request.GET['kelas'])
            subjectOffer = subject_offer.objects.get(pk=request.GET['kelas'])

            teacherData = dtTeamTeaching.objects.filter(teamId_id=subjectOffer.teamTeaching_id)

            studentClassDataCount = len(studentClassData)
            context = {
                'title': 'Kelas Pelajar',
                'breadcumbs': [
                    ['/', 'Manajemen'],
                    ['/', 'Kelas'],
                    [request.META.get('HTTP_REFERER', '/'),
                     "%s [ %s ] " % (subjectOffer.subject_id.name, subjectOffer.teamTeaching_id.name)]
                ],
                'data': studentClassData,
                'allStudent': allStudent,
                'teacherData': teacherData,
                'studentClassDataCount': studentClassDataCount,
                'deptId': userData.dept_id_id,
                'kelasPk': request.GET['kelas']
            }
            return render(request, 'scheduling-vew/master-student-class.html', context)

    @login_required
    def storePelajarKelas(request):
        if request.POST:
            for studentPk in request.POST.getlist('pelajar[]'):
                studentClass = studentInClass.objects.create()
                studentClass.departementId_id = request.POST['deptId']
                studentClass.subjectOfferId_id = request.POST['kelasPk']
                studentClass.studentId_id = studentPk
                studentClass.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    @login_required
    def dropPelajarKelas(request):
        if request.GET:
            studentClass = studentInClass.objects.get(pk=request.GET['studentPk'])
            studentClass.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def scheduleClass(request):
    return render(request, 'scheduling-vew/master-schedule.html')

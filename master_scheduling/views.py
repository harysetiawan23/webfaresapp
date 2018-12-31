from django.shortcuts import render
from .models import studentClass as studentInClass
from master_jadwal.models import subject_offer
from master_user.models import FaresUser
from django.contrib.auth.decorators import login_required
import psutil


# Create your views here.
class controlStudentClass():

    @login_required
    def scheduleClass(request):
        userData = FaresUser.objects.get(pk=str(request.session['userId']))

        subjectOffer = subject_offer.objects.filter(subject_id__dept_id_id=userData.dept_id_id)
        subjectOfferCount = len(subjectOffer)
        mem = psutil.virtual_memory()
        memoryUtils = {
            'percent': mem.percent,
            'av': "%0.2f" % (mem.available / (1024 * 1024 * 1024)),
            'tot': "%0.2f" % (mem.total / (1024 * 1024 * 1024))
        }
        disk = psutil.disk_usage('/')
        diskUtils = {
            'percent': disk.percent,
            'used': "%0.2f" % (disk.used / (1024 * 1024 * 1024)),
            'tot': "%0.2f" % (disk.total / (1024 * 1024 * 1024))
        }

        context = {
            'title': 'Kelas Pelajar',
            'breadcumbs': [
                ['/', 'Home'],
                ['/control/kelas-pelajar', 'Penawaran Mata Pelajaran']
            ],
            'data': subjectOffer,
            'studentClassDataCount': subjectOfferCount,
            'cpu': psutil.cpu_percent(interval=None),
            'mem': memoryUtils,
            'disk': diskUtils
        }
        return render(request, 'scheduling-vew/master-schedule.html', context)

    @login_required
    def studentClass(request):
        if request.GET:
            userData = FaresUser.objects.get(pk=str(request.session['userId']))
            mem = psutil.virtual_memory()
            memoryUtils = {
                'percent': mem.percent,
                'av': "%0.2f" % (mem.available / (1024 * 1024 * 1024)),
                'tot': "%0.2f" % (mem.total / (1024 * 1024 * 1024))
            }
            disk = psutil.disk_usage('/')
            diskUtils = {
                'percent': disk.percent,
                'used': "%0.2f" % (disk.used / (1024 * 1024 * 1024)),
                'tot': "%0.2f" % (disk.total / (1024 * 1024 * 1024))
            }

            allStudent = FaresUser.objects.filter(dept_id_id=userData.dept_id_id)
            studentClassData = studentInClass.objects.filter(subjectOfferId_id=request.GET['kelas'])
            studentClassDataCount = len(studentClassData)
            context = {
                'title': 'Kelas Pelajar',
                'breadcumbs': [
                    ['/', 'Home'],
                    ['/control/kelas-pelajar', 'Pelajar']
                ],
                'data': studentClassData,
                'allStudent':allStudent,
                'studentClassDataCount': studentClassDataCount,
                'cpu': psutil.cpu_percent(interval=None),
                'mem': memoryUtils,
                'disk': diskUtils,
                'deptId': userData.dept_id_id
            }
            return render(request, 'scheduling-vew/master-student-class.html', context)

    # @login_required
    # def masterSubjectOffer(request):
    #
    #
    #     subjectOfferDataCount = len(subjectOfferData)
    #     context = {
    #         'title': 'Penawaran Mata Pelajaran',
    #         'breadcumbs': [
    #             ['/', 'Home'],
    #             ['/jadwal/penawaran', 'Penawaran Mata Pelajaran']
    #         ],
    #         'data': subjectOfferData,
    #         'session': userData,
    #         'subjectOfferCount': subjectOfferDataCount,
    #         'teamTeachingData': teamTeachingData,
    #         'jamPelajaranData': jamPelajaranData,
    #         'subjectOfferData': subjectData,
    #         'daySelect': time.DAYS,
    #         'dataRuang': dataRuang,
    #         'deptId': userData.dept_id_id,
    #         'cpu': psutil.cpu_percent(interval=None),
    #         'mem': memoryUtils,
    #         'disk':diskUtils
    #
    #     }
    #     return render(request, "jadwal-view/master-subject-offer.html", context)
    #
    # @login_required
    # def storeSubjectOffer(request):
    #     if request.POST:
    #         subjectOffer = subject_offer.objects.create()
    #         subjectOffer.departement_id = request.POST['deptId']
    #         subjectOffer.subject_id_id = request.POST['subjectPk']
    #         subjectOffer.classRoomId_id = request.POST['classPk']
    #         subjectOffer.teamTeaching_id_id = request.POST['teamTeachingPk']
    #         subjectOffer.semester = request.POST['semesterData']
    #         subjectOffer.time_id_id = request.POST['jamPk']
    #         subjectOffer.school_year = request.POST['schoolYear']
    #
    #         subjectOffer.save()
    #
    #         return HttpResponseRedirect(reverse('penawaran-mata-pelajaran'))
    #
    # @login_required
    # def updateSubjectOffer(request):
    #     if request.POST:
    #         subjectOffer = subject_offer.objects.get(pk=str(request.POST['subjectOfferPk']))
    #         subjectOffer.subject_id_id = request.POST['subjectPk']
    #         subjectOffer.classRoomId_id = request.POST['classPk']
    #         subjectOffer.teamTeaching_id_id = request.POST['teamTeachingPk']
    #         subjectOffer.semester = request.POST['semesterData']
    #         subjectOffer.time_id_id = request.POST['jamPk']
    #         subjectOffer.school_year = request.POST['schoolYear']
    #
    #         subjectOffer.save()
    #
    #         return HttpResponseRedirect(reverse('penawaran-mata-pelajaran'))
    #
    # @login_required
    # def dropSubjectOffer(request):
    #     if request.GET:
    #         subjectOffer = subject_offer.objects.get(pk=str(request.GET['subjectOfferPk']))
    #         subjectOffer.delete()
    #
    #         return HttpResponseRedirect(reverse('penawaran-mata-pelajaran'))


def scheduleClass(request):
    return render(request, 'scheduling-vew/master-schedule.html')

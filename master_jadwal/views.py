from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import teamTeaching, dtTeamTeaching, shift, subject_offer, time, subject
from master_asset.models import classRoom
from master_user.models import FaresUser
from django.contrib.auth.decorators import login_required
import psutil


# Create your views here.


class controlSubjectOffer():


    @login_required
    def masterSubjectOffer(request):

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

        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        subjectOfferData = subject_offer.objects.filter(departement_id=userData.dept_id_id)
        teamTeachingData = teamTeaching.objects.filter(deptId_id=str(userData.dept_id_id))
        jamPelajaranData = time.objects.filter(departementId_id=str(userData.dept_id_id))
        dataRuang = classRoom.objects.filter(departement=str(userData.dept_id_id))
        subjectData = subject.objects.filter(dept_id_id=str(userData.dept_id_id))
        subjectOfferDataCount = len(subjectOfferData)
        context = {
            'title': 'Penawaran Mata Pelajaran',
            'breadcumbs': [
                ['/', 'Home'],
                ['/jadwal/penawaran', 'Penawaran Mata Pelajaran']
            ],
            'data': subjectOfferData,
            'session': userData,
            'subjectOfferCount': subjectOfferDataCount,
            'teamTeachingData': teamTeachingData,
            'jamPelajaranData': jamPelajaranData,
            'subjectOfferData': subjectData,
            'daySelect': time.DAYS,
            'dataRuang': dataRuang,
            'deptId': userData.dept_id_id,
            'cpu': psutil.cpu_percent(interval=None),
            'mem': memoryUtils,
            'disk':diskUtils

        }
        return render(request, "jadwal-view/master-subject-offer.html", context)

    @login_required
    def storeSubjectOffer(request):
        if request.POST:
            subjectOffer = subject_offer.objects.create()
            subjectOffer.departement_id = request.POST['deptId']
            subjectOffer.subject_id_id = request.POST['subjectPk']
            subjectOffer.classRoomId_id = request.POST['classPk']
            subjectOffer.teamTeaching_id_id = request.POST['teamTeachingPk']
            subjectOffer.semester = request.POST['semesterData']
            subjectOffer.time_id_id = request.POST['jamPk']
            subjectOffer.school_year = request.POST['schoolYear']

            subjectOffer.save()

            return HttpResponseRedirect(reverse('penawaran-mata-pelajaran'))

    @login_required
    def updateSubjectOffer(request):
        if request.POST:
            subjectOffer = subject_offer.objects.get(pk=str(request.POST['subjectOfferPk']))
            subjectOffer.subject_id_id = request.POST['subjectPk']
            subjectOffer.classRoomId_id = request.POST['classPk']
            subjectOffer.teamTeaching_id_id = request.POST['teamTeachingPk']
            subjectOffer.semester = request.POST['semesterData']
            subjectOffer.time_id_id = request.POST['jamPk']
            subjectOffer.school_year = request.POST['schoolYear']

            subjectOffer.save()

            return HttpResponseRedirect(reverse('penawaran-mata-pelajaran'))

    @login_required
    def dropSubjectOffer(request):
        if request.GET:
            subjectOffer = subject_offer.objects.get(pk=str(request.GET['subjectOfferPk']))
            subjectOffer.delete()

            return HttpResponseRedirect(reverse('penawaran-mata-pelajaran'))


class controlTeamTeaching():


    @login_required
    def masterTeamTeaching(request):

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

        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        teamData = teamTeaching.objects.filter(deptId_id=str(userData.dept_id_id))
        teamTeachingData = dtTeamTeaching.objects.filter(teamId__deptId=str(userData.dept_id_id))
        teacherList = FaresUser.objects.filter(isTeacher=True).filter(dept_id_id=userData.dept_id_id)
        teamTeachingCount = len(teamData)
        subjectData = subject.objects.filter(dept_id_id=str(userData.dept_id_id))

        context = {
            'title': 'Team Teaching',
            'breadcumbs': [
                ['/', 'Home'],
                ['/jadwal/team-teaching', 'Team Teaching']
            ],
            'teamData': teamData,
            'session': userData,
            'teacherList': teacherList,
            'teamDetail': teamTeachingData,
            'teamCount': teamTeachingCount,
            'deptId': userData.dept_id_id,
            'subject': subjectData,
            'cpu': psutil.cpu_percent(interval=None),
            'mem': memoryUtils,
            'disk':diskUtils
        }
        return render(request, "jadwal-view/master-team-teaching.html", context)

    @login_required
    def storeTeamTeaching(request):
        if request.POST:
            teamData = teamTeaching.objects.create()
            teamData.deptId_id = request.POST['deptId']
            teamData.name = request.POST['teamName']
            teamData.subjectId_id = request.POST['subjectPk']
            teamData.save()

            return HttpResponseRedirect(reverse('team-teaching'))

    @login_required
    def updateTeamTeaching(request):
        if request.POST:
            teamData = teamTeaching.objects.get(pk=str(request.POST['teamPk']))
            teamData.name = request.POST['teamName']
            teamData.subjectId_id = request.POST['subjectPk']
            teamData.save()

            return HttpResponseRedirect(reverse('team-teaching'))

    @login_required
    def dropTeamTeaching(request):
        if request.GET:
            teamData = teamTeaching.objects.get(pk=str(request.GET['teamPk']))
            teamData.delete()
            return HttpResponseRedirect(reverse('team-teaching'))

    @login_required
    def storeTeacherTeamTeaching(request):
        if request.POST:
            teacherTeamTeaching = dtTeamTeaching.objects.create()
            teacherTeamTeaching.teamId_id = request.POST['teamTeachingPk']
            teacherTeamTeaching.faresUserId_id = request.POST['teacherPk']
            teacherTeamTeaching.save()

            return HttpResponseRedirect(reverse('team-teaching'))

    @login_required
    def dropTeacherTeamTeaching(request):
        if request.GET:
            teacherTeamTeaching = dtTeamTeaching.objects.get(pk=str(request.GET['teacherTeachingPk']))
            teacherTeamTeaching.delete()

            return HttpResponseRedirect(reverse('team-teaching'))


class controlShiftKelas():


    @login_required
    def masterJenisKelas(request):

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

        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        shiftData = shift.objects.filter(departement_id=str(userData.dept_id_id))
        shiftCount = len(shiftData)
        context = {
            'title': 'Jenis Kelas',
            'breadcumbs': [
                ['/', 'Home'],
                ['/jadwal/jenis-kelas', 'Jenis Kelas']
            ],
            'data': shiftData,
            'session': userData,
            'shiftCount': shiftCount,
            'deptId': userData.dept_id_id,
            'cpu': psutil.cpu_percent(interval=None),
            'mem': memoryUtils,
            'disk':diskUtils
        }
        return render(request, "jadwal-view/master-shift-kelas.html", context)

    @login_required
    def storeJenisKelas(request):
        if request.POST:
            jenisKelas = shift.objects.create()
            jenisKelas.name = request.POST['shiftName']
            jenisKelas.departement_id = request.POST['deptId']

            jenisKelas.save()
            return HttpResponseRedirect(reverse('jenis-kelas'))

    @login_required
    def updateJenisKelas(request):
        if request.POST:
            jenisKelas = shift.objects.get(pk=str(request.POST['shiftPk']))
            jenisKelas.name = request.POST['shiftName']
            jenisKelas.save()
            return HttpResponseRedirect(reverse('jenis-kelas'))

    @login_required
    def dropJenisKelas(request):
        if request.GET:
            jenisKelas = shift.objects.get(pk=str(request.GET['shiftPk']))
            jenisKelas.delete()
            return HttpResponseRedirect(reverse('jenis-kelas'))


class controlJamPelajaran():

    @login_required
    def masterJamPelajaran(request):

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

        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        jamPelajaranData = time.objects.filter(departementId_id=str(userData.dept_id_id))
        jamPelajaranDataCount = len(jamPelajaranData)
        context = {
            'title': 'Jam Pelajaran',
            'breadcumbs': [
                ['/', 'Home'],
                ['/jadwal/jam', 'Jam Pelajaran']
            ],
            'hari': time.DAYS,
            'session': userData,
            'shift': shift.objects.filter(departement=str(userData.dept_id_id)),
            'data': jamPelajaranData.order_by('day'),
            'deptId': userData.dept_id_id,
            'jamPelajaranDataCount': jamPelajaranDataCount,
            'cpu': psutil.cpu_percent(interval=None),
            'mem': memoryUtils,
            'disk': diskUtils

        }
        return render(request, "jadwal-view/master-jam-pelajaran.html", context)

    @login_required
    def storejamPelajaran(request):
        print('Store jam Pelajaran')
        print(request.POST['timeStart'])
        if request.POST:
            pass
            jamPel = time.objects.create()
            jamPel.departementId_id = request.POST['deptId']
            jamPel.shift_id_id = request.POST['shiftId']
            jamPel.day = request.POST['dayId']
            jamPel.hour_start = request.POST['timeStart']
            jamPel.hour_stop = request.POST['timeStop']
            jamPel.save()

            return HttpResponseRedirect(reverse('jam-pelajaran'))

    @login_required
    def updatejamPelajaran(request):
        print('Store jam Pelajaran')
        print(request.POST['timeStart'])
        if request.POST:
            pass
            jamPel = time.objects.get(pk=str(request.POST['timePk']))
            jamPel.shift_id_id = request.POST['shiftId']
            jamPel.day = request.POST['dayId']
            jamPel.hour_start = request.POST['timeStart']
            jamPel.hour_stop = request.POST['timeStop']
            jamPel.save()

            return HttpResponseRedirect(reverse('jam-pelajaran'))

    @login_required
    def dropjamPelajaran(request):
        print('Store jam Pelajaran')
        if request.GET:
            pass
            jamPel = time.objects.get(pk=str(request.GET['timePk']))
            jamPel.delete()

            return HttpResponseRedirect(reverse('jam-pelajaran'))

from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import  subject, classRoom
from master_user.models import FaresUser
from django.contrib.auth.decorators import login_required


def master_user(request):
    context = {
        'breadcumbs': [
            ['/', 'Home'],
            ['/master/user', 'Master User']
        ],
        'title': "Master Pengajar",
    }
    return render(request, "asset-view/master-user.html", context)


class controlPelajar():
    # Create your views here.
    @login_required
    def master_pelajar(request):
        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        studetData = FaresUser.objects.filter(dept_id=str(userData.dept_id.id)).filter(isTeacher=False)
        countMale = len(studetData.filter(gender=1))
        countFemale = len(studetData.filter(gender=2))
        try:
            percentMale = (countMale / len(studetData)) * 100
            percentFemale = (countFemale / len(studetData)) * 100

        except Exception as e:
            percentMale = 0
            percentFemale = 0
            print(e)

        context = {
            'breadcumbs': [
                ['/', 'Home'],
                ['/master/pelajar', 'Master Pelajar']
            ],
            'title': "Master Pelajar",
            'data': studetData,
            'totalCount': (countFemale + countMale),
            'maleCount': countMale,
            'femaleCount': countFemale,
            'percentMale': percentMale,
            'percentFemale': percentFemale,
            'deptId': userData.dept_id.id

        }

        return render(request, "asset-view/master-pelajar.html", context)


class controlPelajaran():

    @login_required
    def master_pelajaran(request):
        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        subjectData = subject.objects.filter(dept_id=userData.dept_id.id)
        context = {
            'breadcumbs': [
                ['/', 'Home'],
                ['/master/pelajaran', 'Master Pelajaran']
            ],
            'title': "Master Pelajaran",
            'data': subjectData,
            'deptId': userData.dept_id.id
        }
        return render(request, "asset-view/master-pelajaran.html", context)

    @login_required
    def tambahPelajaran(request):
        print("Tambah Pelajaran")
        print(request.POST['deptId'])
        if request.POST:
            subjectData = subject.objects.create()
            subjectData.name = request.POST['subjectName']
            subjectData.subject_id = request.POST['subjectId']
            subjectData.dept_id_id = request.POST['deptId']
            subjectData.detail = request.POST['detail']

            subjectData.save()

            return HttpResponseRedirect(reverse('master-pelajaran'))

    @login_required
    def ubahPelajaran(request):
        print("Ubah Pelajaran")
        print(request.POST['deptId'])
        if request.POST:
            subjectData = subject.objects.get(pk=request.POST['subjectPk'])
            subjectData.name = request.POST['subjectName']
            subjectData.subject_id = request.POST['subjectId']
            subjectData.dept_id_id = request.POST['deptId']
            subjectData.detail = request.POST['detail']

            subjectData.save()

            return HttpResponseRedirect(reverse('master-pelajaran'))

    @login_required
    def hapusPelajaran(request):
        print("Hapus Pelajaran")
        if request.GET:
            subjectData = subject.objects.get(pk=request.GET['subjectPk'])
            subjectData.delete()

            return HttpResponseRedirect(reverse('master-pelajaran'))


class controlPengajar():

    @login_required
    def master_pengajar(request):
        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        pengajar = FaresUser.objects.filter(isTeacher=True).filter(dept_id=str(userData.dept_id.id))
        countMale = len(pengajar.filter(gender=1))
        countFemale = len(pengajar.filter(gender=2))
        try:
            percentMale = (countMale / len(pengajar)) * 100
            percentFemale = (countFemale / len(pengajar)) * 100

        except Exception as e:
            percentMale = 0
            percentFemale = 0
            print(e)

        context = {
            'breadcumbs': [
                ['/', 'Home'],
                ['/master/pengajar', 'Master Pengajar']
            ],
            'title': "Master Pengajar",
            'data': pengajar,
            'totalCount': (countMale + countFemale),
            'maleCount': countMale,
            'femaleCount': countFemale,
            'percentMale': percentMale,
            'percentFemale': percentFemale,
            'deptId': userData.dept_id.id

        }
        return render(request, "asset-view/master-pengajar.html", context)

    @login_required
    def tambahPengajar(request):
        print('Registered')
        if request.POST:
            user = FaresUser.objects.create_user(request.POST['registerno'], False, request.POST['registerno'])
            user.registred_no = request.POST['registerno']
            user.dept_id_id = request.POST['deptId']
            user.full_name = request.POST['fullname']
            user.gender = request.POST['gender']
            user.isTeacher = True
            user.save()

            return HttpResponseRedirect(reverse('master-pengajar'))

    @login_required
    def dropPengajar(request):
        print('Delete Check')
        if request.GET:
            user = FaresUser.objects.get(pk=str(request.GET['userPk']))
            user.delete()
            return HttpResponseRedirect(reverse('master-pengajar'))

    @login_required
    def updatePengajar(request):
        print(request.POST['userPk'])
        print('Delete Check')
        if request.POST:
            user = FaresUser.objects.get(pk=str(request.POST['userPk']))
            user.full_name = request.POST['fullname']
            user.nick_name = request.POST['nickname']
            user.date_of_birth = request.POST['dateofbirth']
            user.gender = request.POST['gender']
            user.address = request.POST['address']
            user.save()
            return HttpResponseRedirect(reverse('master-pengajar'))


@login_required
class controlRuang():

    @login_required
    def master_ruang(request):
        userData = FaresUser.objects.get(pk=str(request.session['userId']))
        dataRuang = classRoom.objects.filter(departement=str(userData.dept_id_id))
        dataRuangCount = len(dataRuang)
        context = {
            'breadcumbs': [
                ['/', 'Home'],
                ['/master/ruang', 'Master Ruang']
            ],
            'title': "Master Ruang",
            'dataRuang': dataRuang,
            'deptId': userData.dept_id_id,
            'totalRuang': dataRuangCount
        }
        return render(request, "asset-view/master-ruang.html", context)

    @login_required
    def storeRuang(request):
        print("Store Ruang")
        print(request.POST['deptId'])
        if request.POST:
            ruang = classRoom.objects.create()
            ruang.class_name = request.POST['classname']
            ruang.departement_id = request.POST['deptId']
            ruang.save()
            return HttpResponseRedirect(reverse('master-ruang'))

    @login_required
    def updateRuang(request):
        print("Update Ruang")
        if request.POST:
            ruang = classRoom.objects.get(pk=str(request.POST['classPk']))
            ruang.class_name = request.POST['classname']
            ruang.save()
            return HttpResponseRedirect(reverse('master-ruang'))

    @login_required
    def dropRuang(request):
        print("Drop Ruang")
        if request.GET:
            ruang = classRoom.objects.get(pk=str(request.GET['classPk']))
            ruang.delete()
            return HttpResponseRedirect(reverse('master-ruang'))

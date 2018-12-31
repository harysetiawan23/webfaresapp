from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from master_user.models import FaresUser
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import psutil


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:  # <-  no parentheses any more!
        return HttpResponseRedirect(reverse('index'))

    if request.POST:

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            userData = FaresUser.objects.get(pk=str(user))
            request.session['userId'] = str(userData.pk)
            print("USER TRUE")
            return HttpResponseRedirect(reverse('index'))
        else:
            print("USER FALSE")

    return render(request, 'registration/login.html')


def register_user(request):
    print('Registered')
    if request.POST:
        user = FaresUser.objects.create_user(request.POST['registred_no'], False, request.POST['registred_no'])
        user.registred_no = request.POST['registred_no']
        user.dept_id_id = request.POST['deptId']
        user.full_name = request.POST['fullname']
        user.gender = request.POST['gender']
        user.save()

        return HttpResponseRedirect(reverse('master-pelajar'))


def delete_user(request):
    print('Delete Check')
    if request.GET:
        user = FaresUser.objects.get(pk=str(request.GET['userPk']))
        user.delete()
        return HttpResponseRedirect(reverse('master-pelajar'))


def upadate_user(request):
    print(request.POST['userPk'])
    print('Delete Check')
    if request.POST:
        user = FaresUser.objects.get(pk=str(request.POST['userPk']))
        user.registred_no = request.POST['registred_no']
        user.full_name = request.POST['fullname']
        user.nick_name = request.POST['nickname']
        user.date_of_birth = request.POST['dateofbirth']
        user.gender = request.POST['gender']
        user.address = request.POST['address']
        user.save()
        return HttpResponseRedirect(reverse('master-pelajar'))

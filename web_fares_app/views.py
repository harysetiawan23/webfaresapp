from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from master_user.models import FaresUser
from django.core.serializers import serialize
from django.core import serializers
import psutil
import json


@login_required
def index(request):
    currentUser = FaresUser.objects.get(pk=str(request.session['userId']))

    context = {
        'title': 'Dashboard',
        'session': currentUser,
        'cpu': psutil.cpu_percent(interval=None)
    }
    return render(request, "index.html", context)


def systemStat(request):
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
        'title': 'Dashboard',
        'cpu': psutil.cpu_percent(interval=None),
        'mem': memoryUtils,
        'disk': diskUtils,
    }
    return JsonResponse(context, content_type='application/json')


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        error_message = {
            'error': 'Username dan Password tidak boleh kosong'
        }

        return Response(error_message, status=HTTP_400_BAD_REQUEST)

    userId = authenticate(username=username, password=password)

    if not userId:
        error_message = {
            'error': 'User tidak ditemukan'
        }
        return Response(error_message, status=HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=userId)

    userData = FaresUser.objects.get(pk=str(userId))

    USERDATA = {
        'status': True,
        'token': token.key,
        'userPk': token.user.pk
    }

    return HttpResponse(json.dumps(USERDATA), content_type='application/json')


@csrf_exempt
@api_view(['POST'])
def simpleData(request):
    return HttpResponse(
        serializers.serialize("json", [FaresUser.objects.get(pk=request.POST['userPk']),]),
        content_type="application/json"
    )

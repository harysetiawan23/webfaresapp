from django.shortcuts import render
from django.contrib.auth import authenticate
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
from master_user.models import FaresUser
from django.contrib.auth.decorators import login_required
from master_user.models import FaresUser


@login_required
def index(request):
    currentUser = FaresUser.objects.get(pk=str(request.session['userId']))
    context = {
        'title': 'Dashboard',
        'userName':currentUser.nick_name

    }
    return render(request, "index.html", context)


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
        'user': {
            'name': str(userData.full_name),
            'reg_no': str(userData.registred_no),
            'dateOfBirth': str(userData.date_of_birth)
        },
        'token': token.key
    }

    return Response(USERDATA, status=HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def simpleData(request):
    return Response({'data': 'Hell yeah Success'}, status=HTTP_200_OK)

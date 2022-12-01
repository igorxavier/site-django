import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from . import forms
from .models import Clientes

# Create your views here.

def frontpage(request):
    return render(request, 'clientes/pages/frontpage.html')

def kiwify_test_dm(request, mac):

    # Procura o mac e retorna uma resposta

    cliente = Clientes.objects.filter(Q(mac1=mac) | Q(mac2=mac) | Q(mac3=mac) | Q(mac4=mac) | Q(mac5=mac) | Q(mac6=mac)).first()

    if cliente:
        status = 200
        data = {
            'register': True,
            'version': '0.0.1',
            'url': 'https://robozinhos.com.br/83lrfhsr7jfk9'
            }
    else:
        status = 500
        data = {
            'register': False,
            }

    print('Testa se o mac existe')

    return JsonResponse(data=data, status=status)


def kiwify_test(request, mac):
    print('Testa se o mac existe - test')


@csrf_exempt
def kiwify_dm(request):
    print('Recebe um post do download machine da kiwify e cadastra o email')


@csrf_exempt
def kiwify_vmp(request):
    print('Recebe um post do vídeo machine pro da kiwify e cadastra o email')


def hotmart_test(request, mac):

    cliente = Clientes.objects.filter(Q(mac1=mac) | Q(mac2=mac) | Q(mac3=mac) | Q(mac4=mac) | Q(mac5=mac) | Q(mac6=mac)).first()

    if cliente:
        status = 200
        data = {
            'register': True,
            'version': '0.0.8',
            'url': 'https://robozinhos.com.br/20fjnct59ghj39'
            }
    else:
        status = 500
        data = {
            'register': False,
            }

    print('Testa se o mac existe')

@csrf_exempt
def hotmart_rdm(request, mac):
    print('Recebe um post do download machine da Hotmart e cadastra o email')

@csrf_exempt
def hotmart_rvm(request, mac):
    print('Recebe um post do vídeo machine pro da Hotmart e cadastra o email')


@csrf_exempt
def download_machine_post(request):

    print('passou na tentativa de pegar o post')
    received_json_data = json.loads(request.body.decode("utf-8"))

    print(received_json_data)

    if received_json_data['nome'] and received_json_data['email'] and received_json_data['codigo']:

        cliente = Clientes.objects.filter(Q(email_compra=received_json_data['email'])).filter(Q(mac1__exact='') | Q(mac1__isnull=True)).first()


        if cliente:
            cliente.nome = received_json_data['nome']
            cliente.mac1 = received_json_data['codigo']
            cliente.save()
            
            status = 200
            data = {
                'success': True,
                }
        else:
            status = 500
            data = {
                'success': False,
                }
    else:
        status = 500
        data = {
            'success': False,
            }

    return JsonResponse(data=data, status=status)


@csrf_exempt
def video_maker_test_post(request):

    print('passou na tentativa de pegar o post')
    received_json_data = json.loads(request.body.decode("utf-8"))

    print(received_json_data)

    if received_json_data['nome'] and received_json_data['email'] and received_json_data['codigo']:

        cliente = Clientes.objects.filter(Q(email_compra=received_json_data['email'])).filter(Q(mac1__exact='') | Q(mac1__isnull=True)).first()


        if cliente:
            cliente.nome = received_json_data['nome']
            cliente.mac1 = received_json_data['codigo']
            cliente.save()
            
            status = 200
            data = {
                'success': True,
                }
        else:
            status = 500
            data = {
                'success': False,
                }
    else:
        status = 500
        data = {
            'success': False,
            }

    return JsonResponse(data=data, status=status)




def custom_page_not_found_view(request, exception):
    return render(request, "clientes/errors/404.html", status=404)

def custom_error_view(request, exception=None):
    return render(request, "clientes/errors/500.html", status=500)

def custom_permission_denied_view(request, exception=None):
    return render(request, "clientes/errors/403.html", status=403)

def custom_bad_request_view(request, exception=None):
    return render(request, "clientes/errors/400.html", status=400)
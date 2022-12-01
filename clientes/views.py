from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from . import forms
from .models import Clientes

# Create your views here.

def frontpage(request):
    return render(request, 'clientes/pages/frontpage.html')

def kiwify_test_dm(request, mac):

    # Procura o mac e retorna uma resposta

    # if ( 0 < $pod_cliente_video_maker->total() ) {
    #     http_response_code(200);
    #     $arr = [
    #         'register' => true,
    #         'version' => '0.0.8',
    #         'url'=>'https://robozinhos.com.br/20fjnct59ghj39'];
    #     echo json_encode($arr);
    # }else{
    #     http_response_code(500);
    #     $arr = array('register' => false);
    #     echo json_encode($arr);
    # };

    print('Testa se o mac existe')

def kiwify_test(request, mac):
    print('Testa se o mac existe - test')

def kiwify_dm(request, mac):
    print('Recebe um post do download machine da kiwify e cadastra o email')

def kiwify_vmp(request, mac):
    print('Recebe um post do vídeo machine pro da kiwify e cadastra o email')


def hotmart_test(request, mac):

    # Procura o mac e retorna uma resposta

    # if ( 0 < $pod_cliente_video_maker->total() ) {
    #     http_response_code(200);
    #     $arr = [
    #         'register' => true,
    #         'version' => '0.0.8',
    #         'url'=>'https://robozinhos.com.br/20fjnct59ghj39'];
    #     echo json_encode($arr);
    # }else{
    #     http_response_code(500);
    #     $arr = array('register' => false);
    #     echo json_encode($arr);
    # };

    print('Testa se o mac existe')


def hotmart_rdm(request, mac):
    print('Recebe um post do download machine da Hotmart e cadastra o email')

def hotmart_rvm(request, mac):
    print('Recebe um post do vídeo machine pro da Hotmart e cadastra o email')


def download_machine_post(request, mac):
    print('Recebe um post json direto do robozinho, verifica se o email já está no banco e cadastra o mac')

def video_maker_test_post(request, mac):
    print('Recebe um post json direto do robozinho, verifica se o email já está no banco e cadastra o mac')











def custom_page_not_found_view(request, exception):
    return render(request, "clientes/errors/404.html", status=404)

def custom_error_view(request, exception=None):
    return render(request, "clientes/errors/500.html", status=500)

def custom_permission_denied_view(request, exception=None):
    return render(request, "clientes/errors/403.html", status=403)

def custom_bad_request_view(request, exception=None):
    return render(request, "clientes/errors/400.html", status=400)
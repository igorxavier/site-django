from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views

app_name = 'clientes'

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path('kiwify-test-dm/<str:mac>', views.kiwify_test_dm),
    path('kiwify-test/<str:mac>', views.kiwify_test),
    path('kiwify-dm', views.kiwify_dm),
    path('kiwify-vmp', views.kiwify_vmp),


    path('hotmart-test/<str:mac>', views.hotmart_test),
    path('hotmart-rdm', views.hotmart_rdm),
    path('hotmart-rvm', views.hotmart_rvm),
    

    path('robo-download-machine-post', views.download_machine_post),
    path('robo-video-maker-test-post', views.video_maker_test_post),
]

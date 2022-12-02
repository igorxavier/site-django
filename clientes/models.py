from django.contrib.auth.models import User
from django.db import models


class Clientes(models.Model):
    nome                = models.CharField(max_length = 150, default='', blank=True, null=True)
    email               = models.CharField(max_length = 150)
    num_contato         = models.CharField(max_length = 15, blank=True, null=True)
    mac1                = models.CharField(max_length = 150, default='', blank=True, null=True)
    mac2                = models.CharField(max_length = 150, default='', blank=True, null=True)
    mac3                = models.CharField(max_length = 150, default='', blank=True, null=True)
    mac4                = models.CharField(max_length = 150, default='', blank=True, null=True)
    mac5                = models.CharField(max_length = 150, default='', blank=True, null=True)
    mac6                = models.CharField(max_length = 150, default='', blank=True, null=True)
    conta               = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perfil', blank=True, null=True)
    data                = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

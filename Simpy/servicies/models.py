from django.db import models
from django.contrib.auth.models import User
from django.utils import  timezone

# Create your models here.

class SomeTable(models.Model):
    title  = models.CharField('Название', max_length=100)
    text = models.TextField('Описание')

    class Meta:
        verbose_name = 'SomeTable'
        verbose_name_plural = 'SomeTables'
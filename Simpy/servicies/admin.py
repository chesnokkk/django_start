from django.contrib import admin

# Register your models here.

from .models import SomeTable
admin.site.register(SomeTable)
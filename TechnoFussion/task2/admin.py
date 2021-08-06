from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Request, SuppSeq, Labels)
class DefaultAdmins(admin.ModelAdmin):
    pass
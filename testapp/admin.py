from django.contrib import admin
from .models import Company
# Register your models here.
class Companyadmin(admin.ModelAdmin):
    list_display = ["name","ceo","city","ctype"]



admin.site.register(Company,Companyadmin)
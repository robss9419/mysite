from django.contrib import admin
from .models import Machine, Category, Report

admin.site.register(Report)
admin.site.register(Machine)
admin.site.register(Category)

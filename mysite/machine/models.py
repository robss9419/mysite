from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from .validators import MinValueValidator

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nazwa kategorii")
    def __str__(self):
        return self.name

class Machine(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria")
    name = models.CharField(max_length=100, verbose_name="Nazwa maszyny", null=False)
    code = models.CharField(max_length=50, verbose_name="Kod maszyny", null=False)
    mth = models.IntegerField(verbose_name="Motogodziny", null=False)
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name="Data utworzenia")
    def __str__(self):
        return self.name

class Report(models.Model):
    SERVICE_TYPE = (
        ('250', '250mth'),
        ('500', '500mth'),
        ('1000', '1000mth'),
    )
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Kod maszyny", related_name="mach")
    mth = models.IntegerField(verbose_name="Motogodziny", null=False)
    service_type = models.CharField(max_length=4, choices=SERVICE_TYPE, verbose_name="Typ serwisu")
    date_created = models.DateTimeField(
        default=timezone.now, verbose_name="Data utworzenia")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (self.service_type)
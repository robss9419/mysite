from django import forms
from . import models


class MachineForm(forms.ModelForm):
    class Meta:
        model = models.Machine
        fields = "__all__"

class ReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = ('machine', 'mth', 'service_type', 'date_created')




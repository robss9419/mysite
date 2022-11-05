from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Report, Machine
from .forms import MachineForm, ReportForm

class AllMachineView(LoginRequiredMixin, generic.ListView):
    template_name = 'machines.html'
    context_object_name = 'machine_list'

    def get_queryset(self):
        return Machine.objects.order_by('name')

class AllReportView(LoginRequiredMixin, generic.ListView):
    template_name = 'reports.html'
    context_object_name = 'report_list'

    def get_queryset(self):
        return Report.objects.order_by('-date_created')

class MachineReportsView(LoginRequiredMixin, generic.ListView):
    template_name = 'machine_reports.html'
    context_object_name = 'rep_list'

    def get_queryset(self):

        return Report.objects.filter().order_by('-date_created')

@login_required
def machine_detail(request, machine_id):
    machine = Machine.objects.get(id=machine_id)
    return render(request, 'machine.html', {'machine': machine})

@login_required
def report_detail(request, machine_id):
    machine = Machine.objects.get(id=machine_id)
    reports = machine.mach.order_by('-date_created')
    return render(request, 'machine_reports.html', {'machine': machine, 'reports': reports})


@login_required
def update(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.save()
            return redirect('machine-list')
    else:
        form = MachineForm(instance=machine)
    return render(request, 'edit.html', {'form': form})

@login_required
def new_machine(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.save()
            return redirect('machine-list')
    else:
        form = MachineForm()
    return render(request, 'create_machine.html', {'form': form})

@login_required
def new_report(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        machineform = ReportForm(request.POST, instance=machine)
        if form.is_valid():
            report = form.save(commit=False)
            report.owner = request.user
            report.save()
            reportmachine = machineform.save(commit=False)
            reportmachine.save()
            return redirect('machine-list')
    else:
        form = ReportForm(instance=machine)
    return render(request, 'create_report.html', {'form': form})

@login_required
def delete(request, machine_id):
        machine = Machine.objects.get(id=machine_id)
        machine.delete()
        return redirect('machine-list')

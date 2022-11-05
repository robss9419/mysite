from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllMachineView.as_view(), name='machine-list'),
    path('create', views.new_machine, name='create-machine'),
    path('<int:machine_id>', views.machine_detail, name='machine-detail'),
    path('update/<int:machine_id>', views.update, name='update-machine'),
    path('delete/<int:machine_id>', views.delete, name='delete-machine'),
    path('<int:machine_id>/report', views.new_report, name='create-report'),
    path('reports', views.AllReportView.as_view(), name='report-list'),
    path('<int:machine_id>/book', views.report_detail, name='machine-reports')
]
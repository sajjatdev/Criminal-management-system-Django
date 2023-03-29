from django.contrib import admin

from view.models import ReportModel, StationModel


@admin.register(ReportModel)
class ReportAdminView(admin.ModelAdmin):
    list_display = ['ID', 'name', 'phone', 'title', 'create_at', 'status']


@admin.register(StationModel)
class StationListAdminview(admin.ModelAdmin):

    list_display = ['stationName', 'phone', 'phone2', 'address']

from django.contrib import admin

from view.models import ReportModel


@admin.register(ReportModel)
class ReportAdminView(admin.ModelAdmin):
    list_display = ['name', 'phone', 'title', 'create_at']

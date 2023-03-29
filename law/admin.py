from django.contrib import admin

from law.models import CourtModel


@admin.register(CourtModel)
class CourtAdminView(admin.ModelAdmin):

    list_display = ['ID', 'JudgeName', 'CourtName']
    list_filter = ['ID', 'CourtName']

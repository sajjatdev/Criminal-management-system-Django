from django.contrib import admin
from django.utils.html import format_html
from criminal.models import CasesModel, CriminalModel, PunishmentModel


admin.site.site_header = 'Criminal Management'


class PunishmentInline(admin.StackedInline):
    model = PunishmentModel
    can_delete = False
    verbose_name_plural = 'Punishment'
    extra = 1


@admin.register(CriminalModel)
class CriminalAdminView(admin.ModelAdmin):
    inlines = (PunishmentInline, )

    list_display = ['name', 'profile_Photo',
                    'ID_Photo', 'documant_type', 'dateOfBirth', 'caseStatus',]
    list_filter = ['name', 'case__id']

    def caseStatus(self, obj):
        return obj.case.status
    caseStatus.short_description = 'Case Status'

    def profile_Photo(self, x):
        return format_html('<img src="{}" width="70px" height="70px" />'.format(x.image.url))

    profile_Photo.short_description = 'Profile Photo'

    def ID_Photo(self, x):
        return format_html('<img src="{}" width="70px" height="70px" />'.format(x.documant.url))

    ID_Photo.short_description = 'ID Photo'


@admin.register(CasesModel)
class CasesAdminView(admin.ModelAdmin):
    list_display = ['id', 'title', 'userName', 'create_at',  'status']

    def userName(self, obj):
        return obj.user.first_name + " " + obj.user.last_name
    userName.short_description = 'User'

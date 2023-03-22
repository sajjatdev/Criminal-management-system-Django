from django.contrib import admin

from account.models import Account
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import StaffAccountProfile


class StaffProfileInline(admin.StackedInline):
    model = StaffAccountProfile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdminConfig(UserAdmin):

    inlines = (StaffProfileInline, )

    filter_horizontal = ()
    model = Account
    list_display = ['email', 'Name', 'profile_Photo',
                    'card_number', 'ID_Photo', 'date_joined',  'is_active', 'groups',]
    list_filter = []
    search_fields = ['email']
    ordering = ['date_joined']

    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'groups',)
        }),

    )

    add_fieldsets = (
        (None, {
            'fields': ('email',  'password1', 'password2', 'is_active', 'is_staff', 'groups',)
        }),

    )

    def profile_Photo(self, x):
        return format_html('<img src="{}" width="70px" height="70px" />'.format(StaffAccountProfile.objects.get(account=x.id).image.url))

    profile_Photo.short_description = 'Profile Photo'

    def card_number(self, x):
        return StaffAccountProfile.objects.get(account=x.id).cardNumber

    card_number.short_description = "ID Number"

    def ID_Photo(self, x):
        return format_html('<img src="{}" width="70px" height="70px" />'.format(StaffAccountProfile.objects.get(account=x.id).cardImage.url))

    ID_Photo.short_description = 'ID Photo'


admin.site.register(Account, UserAdminConfig)

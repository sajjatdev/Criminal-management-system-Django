from django.contrib.auth.models import Group
from django.contrib import admin

from settings.models import CrimeType, CriminalStatus, Postion, Punishment, Station


admin.site.register(Station)
admin.site.register(Postion)
admin.site.register(Punishment)
admin.site.register(CriminalStatus)
admin.site.register(CrimeType)

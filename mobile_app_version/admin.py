from django.contrib import admin
from .models import MobileAppVersion

class MobileAppVersionAdmin(admin.ModelAdmin):
    list_display = ('manufactor', 'version')

admin.site.register(MobileAppVersion, MobileAppVersionAdmin)

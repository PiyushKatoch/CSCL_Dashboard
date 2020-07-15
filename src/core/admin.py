from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.


class USResource(resources.ModelResource):
    class Meta:
        model = US

class USAdmin(ImportExportModelAdmin):
    pass


class UKResource(resources.ModelResource):
    class Meta:
        model = UK


class UKAdmin(ImportExportModelAdmin):
    pass


class IndiaResource(resources.ModelResource):
    class Meta:
        model = India


class IndiaAdmin(ImportExportModelAdmin):
    pass

admin.site.register(US, USAdmin)
admin.site.register(UK, UKAdmin)
admin.site.register(India, IndiaAdmin)

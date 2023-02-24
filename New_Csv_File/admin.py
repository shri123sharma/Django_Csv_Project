from django.contrib import admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin,ImportExportMixin
from django.contrib import admin
from .models import *
from .resources import *
from import_export.fields import Field
from import_export import resources

# Register your models here.
admin.site.register(Country)
admin.site.register(Hobby)
admin.site.register(Skill)

class PersonDetailAdmin(ImportExportModelAdmin):
    list_display = ('name','mobile','email','gender','mobile','email','aadhaar','country','address',
    'hobby','skill','internal_status')
    resource_class = PersonDetailsAdminResource
admin.site.register(PersonDetail,PersonDetailAdmin)
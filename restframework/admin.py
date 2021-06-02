from django.contrib import admin
from import_export.admin import ImportExportModelAdmin,ImportExportMixin
from .models import Item
# Register your models here.





@admin.register(Item)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('brand','model_no','type_of_computer','assiend_end_user','status','ip_address')
    search_fields = ('name','electoralArea__name')
    list_filter = ['status','brand','type_of_computer']


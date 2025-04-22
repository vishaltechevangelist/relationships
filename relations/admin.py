from django.contrib import admin
from relations.models import Husband, Wife

# Register your models here.
@admin.register(Wife)
class WifeAdmin(admin.ModelAdmin):
    list_display = ['name', 'husband']

@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ['name']
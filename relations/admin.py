from django.contrib import admin
from.models import Husband,Wife

# Register your models here.

admin.site.register(Husband)

@admin.register(Wife)
class WifeAdmin(admin.ModelAdmin):
    list_display=['name','husband']

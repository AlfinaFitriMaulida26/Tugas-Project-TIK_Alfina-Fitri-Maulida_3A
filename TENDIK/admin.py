from django.contrib import admin
from TENDIK.models import Tendik

# Register your models here.

class TendikAdmin(admin.ModelAdmin):
    list_display = ['no', 'nama_jabatan', 'nama', 'nip']
    search_fields = ['no', 'nama_jabatan']

admin.site.register(Tendik, TendikAdmin)

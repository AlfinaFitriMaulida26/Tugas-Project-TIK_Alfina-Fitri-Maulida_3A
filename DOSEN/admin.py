from django.contrib import admin
from DOSEN.models import Dosen

# Register your models here.

class DosenAdmin(admin.ModelAdmin):
    list_display = ['nip', 'nidn', 'nama', 'jabatan', 'email', 'foto']
    search_fields = ['nip', 'nama']

admin.site.register(Dosen, DosenAdmin)

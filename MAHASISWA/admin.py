from django.contrib import admin
from MAHASISWA.models import Mahasiswa

# Register your models here.

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['nim', 'nama', 'ttl', 'email', 'fakultas', 'prodi', 'alamat', 'foto']
    search_fields = ['nim', 'nama']

admin.site.register(Mahasiswa, MahasiswaAdmin)

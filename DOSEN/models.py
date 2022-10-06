from django.db import models

# Create your models here.

class Dosen(models.Model):
    nip = models.CharField(max_length=50)
    nidn = models.CharField(max_length=50, null=True)
    nama = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='media/',blank=True, null=True)


    def _str_(self):
        return "{}".format(self.nama)

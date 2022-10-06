from django.db import models

# Create your models here.

class Tendik(models.Model):
    no = models.CharField(max_length=100)
    nama_jabatan = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    nip = models.CharField(max_length=100)


    def _str_(self):
        return "{}".format(self.nama)

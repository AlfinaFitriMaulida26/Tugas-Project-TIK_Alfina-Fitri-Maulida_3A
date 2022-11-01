from dataclasses import field
from django.forms import ModelForm
from django import forms
from MAHASISWA.models import Mahasiswa

class FormMahasiswa(ModelForm):
    class Meta:
       model = Mahasiswa
       fields = ['nim', 'nama', 'ttl', 'email', 'fakultas', 'prodi', 'alamat']

       widgets = {
        'nim' : forms.NumberInput({'class':'form-control'}),
        'nama' : forms.TextInput({'class':'form-control'}),
        'ttl' : forms.TextInput({'class':'form-control'}),
        'email' : forms.TextInput({'class':'form-control'}),
        'fakultas' : forms.TextInput({'class':'form-control'}),
        'prodi' : forms.TextInput({'class':'form-control'}),
        'alamat' : forms.TextInput({'class':'form-control'}),
       }
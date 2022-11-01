from django.shortcuts import render, redirect
from MAHASISWA.models import Mahasiswa
from MAHASISWA.forms import FormMahasiswa, Mahasiswa
from django.contrib import messages

# Create your views here.

def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()

    messages.success(request, "Data deleted successfully!")

    return redirect('mahasiswa')

def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST: 
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully!")
            return redirect('ubah_mahasiswa', id_mahasiswa=id_mahasiswa)
    else: 
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form': form, 
            'mahasiswa': mahasiswa,
        }
        return render(request, template, konteks)


def mahasiswa(request):

    context = {
        'student': Mahasiswa.objects.all()
    }    
    return render(request, 'indexmahasiswa.html', context)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data saved successfully!"
            context = {
                'form' : form, 
                'pesan' : pesan,
            }
            return render(request, 'tambah-mahasiswa.html', context)

    else:
        form = FormMahasiswa()

    context = {
        'form' : form,
    }

    return render(request, 'tambah-mahasiswa.html', context)
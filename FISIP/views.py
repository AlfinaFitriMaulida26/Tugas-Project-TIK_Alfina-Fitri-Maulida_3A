from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judul = ["Studi Administrasi Publik", "Studi Ilmu Komunikasi", "Studi Ilmu Pemerintahan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfisip.html', konteks)
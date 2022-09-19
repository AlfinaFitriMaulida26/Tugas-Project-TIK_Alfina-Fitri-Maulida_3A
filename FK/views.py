from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = ["Kedokteran", "Keperawatan S1", "Keperawatan D3", "S1 Gizi", "Ilmu Keolahragaan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfK.html', konteks)

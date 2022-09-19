from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judul = ["Pendidikan Nonformal", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Biologi", "Pendidikan Matematika", "Pendidikan Guru Sekolah Dasar", "Pendidikan Guru PAUD", "Bimbingan dan Konseling", "Pendidikan Fisika", "Pendidikan Ilmu Pengetauan Alam", "Pendidikan Kimia", "Pendidikan Khusus", "Pendidikan Pancasila dan Kewarganegaraan", "Pendidikan Sejarah", "Pendidikan Seni dan Pertunjukan", "Pendidikan Sosiologi", "Pendidikan Vokasional Teknik Elektro", "Pendidikan Vokasional Teknik Mesin"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfkip.html', konteks)

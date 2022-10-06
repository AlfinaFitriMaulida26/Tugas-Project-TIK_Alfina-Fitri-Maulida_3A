from django.shortcuts import render
from DOSEN.models import Dosen

# Create your views here.

def dosen(request):

    context = {
        'teacher': Dosen.objects.all()
    }    
    return render(request, 'indexdosen.html', context)

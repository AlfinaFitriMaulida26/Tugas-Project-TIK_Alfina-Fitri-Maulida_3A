from django.shortcuts import render
from TENDIK.models import Tendik

# Create your views here.

def tendik(request):

    context = {
        'teacher': Tendik.objects.all()
    }    
    return render(request, 'indextendik.html', context)

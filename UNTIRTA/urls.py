"""UNTIRTA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FAPER.views import prodi1
from FEB.views import prodi2
from FH.views import prodi3
from FISIP.views import prodi4
from FK.views import prodi5
from FKIP.views import prodi6
from FT.views import prodi7
from PASCASARJANA.views import prodi8
from PROFIL.views import profil



urlpatterns = [
    path('admin/', admin.site.urls),
    path('FAPER/', prodi1),
    path('FEB/', prodi2),
    path('FH/', prodi3),
    path('FISIP/', prodi4),
    path('FK/', prodi5),
    path('FKIP/', prodi6),
    path('FT/', prodi7),
    path('PASCASARJANA/', prodi8),
    path('PROFIL/', profil),
    
   
]

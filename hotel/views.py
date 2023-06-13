from django.shortcuts import render
from . models import Villa, Genel, Havuz,Galleryv, Aktivite, Restoran, Spa, Food
 



def home(request):
    villas = Villa.objects.all()
    genels = Genel.objects.all()
    havuzs = Havuz.objects.all()
    galleryvs = Galleryv.objects.all()
    aktivites = Aktivite.objects.all()
    restorans = Restoran.objects.all()
    spas = Spa.objects.all()
    foods = Food.objects.all()
    return render(request, 'hotel/home.html', {"villas":villas, "genels":genels, "havuzs":havuzs, "galleryvs":galleryvs, "aktivites":aktivites, "restorans":restorans, "spas":spas, "foods":foods })

# Create your views here.

from django.shortcuts import render
from . models import Villa, Genel, Havuz,Galleryvilla, Aktivite, Restoran, Spa, Food
 



def home(request):
    villas = Villa.objects.all()
    genels = Genel.objects.all()
    havuzs = Havuz.objects.all()
    galleryvs = Galleryvilla.objects.all()
    aktivites = Aktivite.objects.all()
    restorans = Restoran.objects.all()
    spas = Spa.objects.all()
    foods = Food.objects.all()
    return render(request, 'hotel/home.html', {"villas":villas, "genels":genels, "havuzs":havuzs, "galleryvs":galleryvs, "aktivites":aktivites, "restorans":restorans, "spas":spas, "foods":foods })

# Create your views here.
def lalila(request):
    villah = Galleryvilla.objects.filter(name ="lalila")
    villainfo = Villa.objects.all()
    villas = Villa.objects.all()
    return render(request, 'hotel/lalila.html',{"villah":villah, "villainfo": villainfo, "villas":villas})
def amarila(request):
    villah = Galleryvilla.objects.filter(name="amarila")
    villas = Villa.objects.all()
    villainfo = Villa.objects.all()
    return render(request, 'hotel/amarila.html',{"villah":villah, "villainfo": villainfo,"villas":villas})
def palaya(request):
    villah = Galleryvilla.objects.filter(name="palaya")
    villainfo = Villa.objects.all()
    villas = Villa.objects.all()
    return render(request, 'hotel/palaya.html',{"villah":villah, "villainfo": villainfo, "villas":villas})
def thegrand(request):
    villah = Galleryvilla.objects.filter(name="thegrand")
    villainfo = Villa.objects.all()
    villas = Villa.objects.all()
    return render(request, 'hotel/thegrand.html',{"villah":villah, "villainfo": villainfo, "villas":villas})
def larensignature(request):
    villah = Galleryvilla.objects.filter(name="larensignature")
    villainfo = Villa.objects.all()
    villas = Villa.objects.all()
    return render(request, 'hotel/larensignature.html',{"villah":villah, "villainfo": villainfo, "villas":villas})

def food (request):
    
    villas = Villa.objects.all()
    genels = Genel.objects.all()
    havuzs = Havuz.objects.all()
    galleryvs = Galleryvilla.objects.all()
    aktivites = Aktivite.objects.all()
    restorans = Restoran.objects.all()
    spas = Spa.objects.all()
    foods = Food.objects.all()
    return render (request, 'hotel/food.html',{ "villas":villas, "genels":genels, "havuzs":havuzs, "galleryvs":galleryvs, "aktivites":aktivites, "restorans":restorans, "spas":spas, "foods":foods})

def activity (request):
    genels = Genel.objects.all()
    havuzs = Havuz.objects.all()
    galleryvs = Galleryvilla.objects.all()
    aktivites = Aktivite.objects.all()
    restorans = Restoran.objects.all()
    spas = Spa.objects.all()
    act = Aktivite.objects.all()
    return render (request, 'hotel/activity.html' , { "genels":genels, "havuzs":havuzs, "galleryvs":galleryvs, "aktivites":aktivites, "restorans":restorans, "spas":spas,"act":act })

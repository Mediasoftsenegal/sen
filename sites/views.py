from django.shortcuts import render

# Create your views here.

def accueil_view(request):
    return render(request, 'accueil.html')

def objectifs_view(request):
    return render(request,'objectifs.html')

def presentation_view(request):
    return render(request,"presentation.html")

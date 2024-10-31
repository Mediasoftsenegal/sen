import requests
from django.shortcuts import render
from .models import articles
from django.core.paginator import Paginator


# Create your views here.

def accueil_view(request):
    article_vedette = articles.objects.order_by ('-date_publication')[:3] 
    return render(request,'accueil.html', {'article':article_vedette})

def actualites_view(request):
    articles_actu  = articles.objects.order_by ('-date_publication')
    paginator = Paginator(articles_actu,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'actualites/actualites.html', {'page_obj': page_obj})  

def lastnew_view(request):
    derniers_articles  = articles.objects.order_by ('-date_publication')[:3]
    context = {'derniers_articles ': derniers_articles }
    return render(request,'actualites/articles_detail.html', context)

def articles_detail_view(request, articles_id):
    article = articles.objects.get(id=articles_id)
    return render(request, 'actualites/articles_detail.html', {'article' : article})
    
def objectifs_view(request):
    return render(request,'objectifs.html')

def presentation_view(request):
    return render(request,'presentation.html')

def generale_view(request):
    return render(request,'presentation/generale.html')

def missions_objectifs_view(request):
    return render(request,'presentation/missions_objectifs.html')

def organisations_view(request):
    return render(request,'presentation/organisations.html')

def historique_view(request):
    return render(request,'presentation/historique.html')

def contexte_view(request):
    return render(request,'presentation/contexte.html')

def equipe_view(request):
    return render(request,'presentation/equipe.html')

def interventions_view(request):
    return render(request,'interventions.html')

def produits_services_view(request):
    return render(request,'interventions/produits_services.html')

def conditions_octroi_view(request):
    return render(request,'interventions/conditions_octroi.html')

def suivi_evaluation_view(request):
    return render(request,'interventions/suivi_evaluation.html')

def criteres_selection_view(request):
    return render(request,'interventions/criteres_selection.html')

def depot_demande_view(request):
    return render(request,'interventions/depot_demande.html')

def partenariat_view(request):
    return render(request,'partenariat.html')

def principes_view(request):
    return render(request,"partenariat/principes.html")

def reseau_view(request):
    return render(request,"partenariat/reseau.html")

def cdmp_view(request):
    return render (request,'partenariat/cdmp.html')
def cdmps_view(request):
    return render (request,'partenariat/cdmps.html')
def ligne_refinancement_view(request):
    return render (request,'partenariat/ligne_refinancement.html')
def cible_view(request):
    return render (request,'partenariat/cible.html')
def caracteristiques_view(request):
    return render (request,'partenariat/caracteristiques.html')
def depots_view(request):
    return render (request,'partenariat/depots.html')
def contact_view(request):
    return render(request,"contact.html")

# def mavue(request) :
#     objet = articles.objects.get(id=1)
#     return render(request,'actualites.html', {'objet':objet})

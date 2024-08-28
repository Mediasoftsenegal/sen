from django.shortcuts import render
from django.core.paginator import Paginator
from .models import articles
# Create your views here.

def accueil_view(request):
    article_vedette = articles.objects.order_by('-date_publication')[:3] 
    return render(request,'accueil.html',{'article':article_vedette})
   
def actualites_view(request):
    articles_list  = articles.objects.order_by('-date_publication') 
    paginator  = Paginator(articles_list,10)
    
    page_number = request.GET.get('page')
    article = paginator.get_page(page_number)
    
    context = {
        'article': article,
    }
                                  
    return render(request,'actualités/actualites.html', context)  
    
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

def articles_detail_view(request, articles_id):
     article = articles.objects.get(id=articles_id)
     return render(request, 'actualités/articles_detail.html', {'article' : article})

def contact_view(request):
    return render(request,"contact.html")
 
     
def test_view(request):
    return render(request,'test.html')   

def test2_view(request):
    return render(request,'test2.html')   

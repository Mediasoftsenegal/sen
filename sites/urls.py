# myapp/urls.py

from django.urls import path

from .views import accueil_view,objectifs_view,presentation_view,interventions_view,partenariat_view,actualites_view,depot_demande_view,articles_detail_view,contact_view,produits_services_view,conditions_octroi_view,suivi_evaluation_view,criteres_selection_view,generale_view,missions_objectifs_view,organisations_view,historique_view,contexte_view,equipe_view,principes_view,reseau_view,cdmp_view,cdmps_view,depots_view,caracteristiques_view,cible_view,ligne_refinancement_view,lastnew_view



urlpatterns = [
    path('', accueil_view, name='accueil'),
    path('objectifs/', objectifs_view, name='objectifs'),
    path('presentation/',presentation_view, name='presentation'),
    path('presentation/generale',generale_view, name='generale'),
    path('presentation/missions_objectifs', missions_objectifs_view, name='missions_objectifs'),
    path('presentation/organisations', organisations_view, name='organisations'),
    path('presentation/historique', historique_view, name='historique'),
    path('presentation/contexte', contexte_view, name='contexte'),
    path('presentation/equipe', equipe_view, name='equipe'),
    path('interventions/', interventions_view, name='interventions'),
    path('interventions/produits_services', produits_services_view, name='produits_services'),
    path('interventions/conditions_octroi', conditions_octroi_view, name='conditions_octroi'),
    path('interventions/suivi_evaluation', suivi_evaluation_view, name='suivi_evaluation'),
    path('interventions/criteres_selection', criteres_selection_view, name='criteres_selection'),
    path('interventions/depot_demande', depot_demande_view, name='depot_demande'),
    path('partenariat/', partenariat_view, name='partenariat'),
    path('partenariat/principes', principes_view, name='principes'),
    path('partenariat/reseau', reseau_view, name='reseau'),   
    path('partenariat/cdmp', cdmp_view, name='cdmp'),
    path('partenariat/cdmps', cdmps_view, name='cdmps'),
    path('partenariat/depots', depots_view, name='depots'),
    path('partenariat/caracteristiques', caracteristiques_view, name='caracteristiques'),
    path('partenariat/cible', cible_view, name='cible'),
    path('partenariat/ligne_refinancement', ligne_refinancement_view, name='ligne_refinancement'),     
    path('actualites/actualites', actualites_view, name='actualites'),
    path('actualites/<int:articles_id>/',articles_detail_view,name ='articles_detail'),
    path('actualites/articles_detail/',lastnew_view,name ='articles_detail'),
    path('contact/', contact_view, name ='contact'),
]

"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from backend import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('afficheDocument/<str:user>', views.get_document),
    path('afficheUtilisateur/<str:user>', views.get_user),
    path('afficheRdv/<str:id>', views.get_rdv),
    path('afficheRdvTous/', views.get_rdv_tous),
    path('afficheChef/<str:user>', views.get_chef),
    path('updateRdv/<str:id>', views.update_rdv),
    path('afficheArrondissement/', views.get_arrondissement),
    path('afficheDistrict/', views.get_district_all),
    path('afficheUtilisateurTout/', views.get_utilisateur_tout),
    path('afficheArrondissementChef/', views.get_arrondissement_chef),
    path('afficheArrondissementChefTout/', views.get_chef_tout),
    path('supprimerDocument/<str:user>', views.delete_document),
    path('supprimerUtilisateur/<str:user>', views.delete_utilisateur),
    path('supprimerChef/<str:user>', views.delete_chef),
    path('supprimerArrondissement/<str:user>', views.delete_arrondissements),
    path('supprimerRegion/<str:user>', views.delete_region),
    path('supprimerDistrict/<str:user>', views.delete_district),
    path('updateDocument/<str:user>', views.update_document),
    path('updateChef/<str:user>', views.update_chef),
    path('updateUtilisateur/<str:user>', views.update_utilisateur),
    path('updateArrondissement/<int:user>', views.update_arrondissements),
    path('updateRegion/<int:user>', views.update_regions),
    path('updateDistrict/<int:user>', views.update_district),
    path("", views.index, name="index"),
    path("api_connexion/", views.connexion, name="connexion"),
    path("api_insertion_arrondissement/", views.ajout_arrondissement, name="arrondissement"),
    path("api_insertion_region/", views.ajout_region),
    path("api_insertion_district/", views.ajout_district),
    path("api_connexionChef/", views.connexion_chef, name="connexionChef"),
    path("api_inscription/", views.inscription, name="inscription"),
    path("api_inscriptionChef/", views.inscription_chef, name="inscriptionChef"),
    path("api_demande/", views.envoieDemande, name="inscription"),
    path("api_code/", views.insertion_verif, name="code"),
    path("api_codeVerif/", views.get_verif, name="code"),
    
    # crud pub
    path("api_ajout_pub/", views.ajout_pub, name="ajout_pub"),
    path("api_affiche_pub/", views.get_pub_tout, name="ajout_pub"),
    path("api_affiche_pub_simple/<int:id>", views.get_pub_simple, name="affiche_pub_simple"),
    path("api_delete_pub/<int:id>", views.delete_pub),
    path("api_modif_pub/<int:id>", views.modif_pub),
    # fin pub
    
    
    #liker
    path("api_liker/", views.ajout_reaction),
    
    #commenter
    path("api_commenter/<int:id>", views.ajout_commentaire),
    path("api_get_comment/<int:ids>", views.get_commentaire_simple),
    
    # notification
    path("api_notification/<str:id>", views.get_notification_simple),
    path("api_notification_non_lue/<str:id>", views.get_notification_non_lue),
    path("api_notification_lire/<str:id>",views.set_notification_lue),
    
    #gestion de demande
    path("api_liste_demande_arrond/<str:id>", views.get_demande_arrondissement),
    path("api_refuser_demande/<str:id>", views.refuser_demande_arrondissement),
    path("api_accepter_demande/<str:id>", views.accepter_demande_arrondissement),
    path("api_stat_arrondissement_chef/<str:id>", views.stat_arrondissement_chef),
    path("api_stat_arrondissement_tous/<int:id>", views.stat_arrondissement_tous),
    path("api_stat_utilisateur_tous/", views.stat_utilisateur_tous),
    path("api_stat_utilisateur_arrond/<str:id>/<int:anne>", views.stat_utilisateur_arrond),
    path("api_stat_utilisateur_arrond_tous/<int:anne>", views.stat_utilisateur_arrond_tous),
    path("ajouter_retour/<str:id>", views.ajouter_retour),
    path("voir_retour/", views.voir_retour),
    
    
    #region et district 
    path("get_district/<str:id>", views.get_district),
    path("get_region/", views.get_region),
    path("get_arrond_district/<str:id>", views.get_arrondissement_par_district),
    path("get_arrond_district_libre/<str:id>", views.get_arrondissement_par_district_libre),
]

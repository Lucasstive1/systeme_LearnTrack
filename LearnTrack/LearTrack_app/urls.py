from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('comments/', views.comments, name="comments"),
    path('faq/', views.faq, name="faq"),
    path('inscription/', views.inscription, name="inscription"),
    path('connexion/', views.connexion, name="connexion"),
    path('epreuve/', views.epreuve, name="epreuve"),
    path('enregistrer_utilisateur/', views.enregistrer_utilisateur, name="enregistrer_utilisateur"),
    path('historique_user/', views.historique_user, name="historique_user"),
    
]
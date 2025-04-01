from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
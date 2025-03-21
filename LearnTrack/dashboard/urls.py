from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name="add_course"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('historique_epreuve/', views.historique_epreuve, name="historique_epreuve"),
    path('update_document/<int:document_id>/', views.update_document, name='update_document'),
    path('delete_document/<int:document_id>/', views.delete_document, name='delete_document'),
]

# Servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

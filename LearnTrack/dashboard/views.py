from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Document
import hashlib
import os
from django.http import JsonResponse

def get_file_hash(file):
    """Retourne le hash SHA256 du contenu du fichier."""
    hasher = hashlib.sha256()
    for chunk in file.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()

def add_course(request):
    if request.method == 'POST':
        matiere = request.POST.get('matiere')
        filiere = request.POST.get('filiere')
        specialite = request.POST.get('specialite')
        type_document = request.POST.get('type')
        niveau = request.POST.get('niveau')
        file = request.FILES.get('file')
        
        
        
        # Vérifier l'extension du fichier
        allowed_extensions = ['.pdf', '.docx', '.pptx']
        file_extension = os.path.splitext(file.name)[1].lower()
        if file_extension not in allowed_extensions:
            messages.error(request, "Format non supporté. Formats acceptés: PDF, DOCX, PPTX.")
            return redirect('add_course')
        
        # Vérifier la taille du fichier (max 25MB)
        if file.size > 25 * 1024 * 1024:
            messages.error(request, "Le fichier est trop volumineux (max 25MB).")
            return redirect('add_course')

        # Calculer le hash du fichier
        file_hash = get_file_hash(file)

        # Vérifier si un document avec le même contenu existe déjà
        if Document.objects.filter(file_hash=file_hash).exists():
            messages.error(request, "Ce document existe déjà sur la plateforme.")
            return redirect('add_course')

        # Enregistrement du document
        document = Document(
            matiere=matiere,
            filiere=filiere,
            specialite=specialite,
            type_document=type_document,
            niveau=niveau,
            file=file,
            file_hash=file_hash
        )
        document.save()

        messages.success(request, "Document ajouté avec succès !")
        return redirect('add_course')
        
        
    return render(request, "backend/autres/ajouter_epreuve.html")


def dashbord(request):
    return render(request, "backend/dashbord.html")


def historique_epreuve(request):
    documents = Document.objects.all().order_by('-date')
    return render(request, "backend/autres/historique_epreuve.html", {'documents': documents})


def update_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    
    if request.method == 'POST':
        # Récupérer les nouvelles informations depuis le formulaire
        document.matiere = request.POST.get('matiere')
        document.filiere = request.POST.get('filiere')
        document.specialite = request.POST.get('specialite')
        document.type_document = request.POST.get('type')
        document.niveau = request.POST.get('niveau')

        # Vérification si un fichier a été téléchargé
        file = request.FILES.get('file')
        if file:
            # Vérifier l'extension du fichier
            allowed_extensions = ['.pdf', '.docx', '.pptx']
            file_extension = os.path.splitext(file.name)[1].lower()
            if file_extension not in allowed_extensions:
                messages.error(request, "Format non supporté. Formats acceptés: PDF, DOCX, PPTX.")
                return redirect('update_document', document_id=document.id)
            
            # Vérifier la taille du fichier (max 25MB)
            if file.size > 25 * 1024 * 1024:
                messages.error(request, "Le fichier est trop volumineux (max 25MB).")
                return redirect('update_document', document_id=document.id)

            # Mettre à jour le fichier
            document.file = file

        # Sauvegarder les modifications
        document.save()
        
        messages.success(request, "Document modifié avec succès !")
        return redirect('historique_epreuve')  # Rediriger vers l'historique des épreuves
    
    # Pour la méthode GET, afficher le formulaire avec les données actuelles du document
    return render(request, "backend/autres/update_document.html", {'document': document})

    
    
def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.is_active = False  # Marquer le document comme désactivé
    document.save()
    
    messages.success(request, "Document désactivé avec succès !")
    return redirect('historique_epreuve')



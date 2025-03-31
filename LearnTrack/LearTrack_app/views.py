from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dashboard.models import Document
from LearTrack_app.models import CustomUser
from django.contrib.auth.models import Group

# Page d'accueil
def index(request):
    return render(request, 'fontend/index.html')

# Page À propos
def about(request):
    return render(request, 'fontend/autres/about.html')

# Page des commentaires
def comments(request):
    return render(request, 'fontend/autres/comments.html')

# Page FAQ
def faq(request):
    return render(request, 'fontend/autres/faq.html')

# Inscription
def inscription(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        # Validation email
        try:
            validate_email(email)
        except:
            messages.error(request, "Veuillez entrer une adresse email valide (example@gmail.com).")
            return redirect('inscription')

        # Vérification des mots de passe
        if password != repassword:
            messages.error(request, "Les deux mots de passe ne correspondent pas.")
            return redirect('inscription')

        # Vérification de l'existence de l'utilisateur
        if User.objects.filter(Q(email=email) | Q(username=name)).exists():
            messages.error(request, f"Un utilisateur avec l'email {email} ou le nom {name} existe déjà.")
            return redirect('inscription')

        # Création de l'utilisateur
        user = User(username=name, email=email)
        user.set_password(password)  # Utilisation correcte du hachage du mot de passe
        user.save()

        messages.success(request, "Inscription réussie ! Connectez-vous à votre compte.")
        return redirect('connexion')

    return render(request, 'fontend/autres/inscription.html')

# Connexion
def connexion(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                messages.success(request, "Connexion réussie avec succès !")
                return redirect('epreuve')
            else:
                messages.error(request, "Mot de passe ou email invalide, veuillez réessayer.")
        else:
            messages.error(request, "Aucun compte trouvé avec cet email.")

    return render(request, 'fontend/autres/connexion.html')

# Page des épreuves (nécessite une connexion)
@login_required(login_url='connexion')
def epreuve(request):
    documents = Document.objects.all()
    return render(request, 'fontend/autres/epreuve.html', {'documents': documents})



def enregistrer_utilisateur(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        role = request.POST.get('role')
        password = request.POST.get('password')
        
        # validation de l'email
        try:
            validate_email(email)
        except:
            messages.error(request, "Veuillez entrer une adresse email valide.")
            return redirect('enregistrer_utilisateur')
        
         # Vérification de l'existence de l'utilisateur
        if CustomUser.objects.filter(Q(email=email) | Q(username=username)).exists():
            messages.error(request, "Un utilisateur avec cet email ou ce nom existe déjà.")
            return redirect('enregistrer_utilisateur')
        
        # Création de l'utilisateur
        user = CustomUser.objects.create_user(username=username, email=email, password=password, phone_number=phone_number)
        
         # Attribution du groupe selon le rôle sélectionné
        if role:
            group, created = Group.objects.get_or_create(name=role)
            user.groups.add(group)
        
        messages.success(request, "Utilisateur ajouté avec succès !")
        return redirect('enregistrer_utilisateur')
        
        
    
    return render(request, 'backend/autres/add_users.html')


def historique_user(request):
    users = CustomUser.objects.all()
    return render(request, 'backend/autres/historique_user.html', {'users': users})
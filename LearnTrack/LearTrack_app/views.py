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
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
User = get_user_model()  # Utilise le modèle défini dans settings.py


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
        if User.objects.filter(email=email).exists() or User.objects.filter(username=name).exists():
            messages.error(request, f"Un utilisateur avec l'email {email} ou le nom {name} existe déjà.")
            return redirect('inscription')

        # Création de l'utilisateur
        user = User.objects.create_user(username=name, email=email, password=password)  # ✅ Création correcte
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
        username = request.POST.get('username', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()
        role = request.POST.get('role', 'Utilisateur') 
        
        errors = []

        # Vérifier si les valeurs ne sont pas vides
        if not username or not phone or not password or not email:
            errors.append("Tous les champs doivent être remplis.")

        # Vérifications de la validité des champs (uniquement si les valeurs ne sont pas None)
        if username and not re.match(r'^[a-zA-Z0-9_]+$', username):
            errors.append("Le nom d'utilisateur ne doit contenir que des lettres, chiffres et underscore.")
        if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            errors.append("Format d'email invalide.")

        # Vérification unicité des données
        if CustomUser.objects.filter(email=email).exists():
            errors.append("L'email existe déjà.")
        if CustomUser.objects.filter(phone=phone).exists():
            errors.append("Le numéro de téléphone est déjà utilisé.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'backend/autres/register.html')

        # Création de l'utilisateur
        user = CustomUser.objects.create(
            username=username,
            email=email,
            role=role,
            phone=phone,
            password=make_password(password)
        )
        
        messages.success(request, "Utilisateur ajouté avec succès !")
        return redirect('enregistrer_utilisateur')
    return render(request, 'backend/autres/add_users.html')


def historique_user(request):
    users = CustomUser.objects.all()
    return render(request, 'backend/autres/historique_user.html', {'users': users})

def deconnexion(request):
    logout(request)  # Déconnecte l'utilisateur
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('connexion')  # Redirige vers la page d'accueil
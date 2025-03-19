# Guide de Configuration du Projet 

Ce guide doit aider à configurer  ton projet de ton cote donc lire bien ceci et execute les code en ordre

## 1. Clone le dépôt

Clonez le dépôt GitHub sur votre machine :

```bash

git clone https://github.com/Lucasstive1/systeme_LearnTrack.git
cd 

# Créer l'environnement virtuel nommé 'venv'
python -m venv venv

# Activer l'environnement virtuel
venv\Scripts\activate

# Installer Django via pip
pip install django

# Installer les dépendances à partir du fichier requirements.txt
pip install -r requirements.txt


# Lancer le serveur Django (assurez-vous que manage.py est présent)
python manage.py runserver

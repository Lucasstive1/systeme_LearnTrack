from django.db import models
import hashlib
# Create your models here.

class Document(models.Model):
    TYPES_CHOICES = [
       ('epreuve_corrigee', 'Épreuve corrigée'),
       ('epreuve_non_corrigee', 'Épreuve non corrigée'),
       ('cours', 'Cours'),
    ]
    
    LEVEL_CHOICES = [
        ('bts_dut', 'Bts dut'),
        ('licence', 'Licence'),
        ('master_1', 'Master 1'),
        ('master_2', 'master 2'),
        ('doctorat', 'Doctoratt'),
    ]
    
    matiere = models.CharField(max_length=255)
    filiere = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)
    type_document = models.CharField(max_length=80, choices = TYPES_CHOICES)
    niveau = models.CharField(max_length=80, choices = LEVEL_CHOICES, default='Bts dut', null=True)
    file = models.FileField(upload_to='documents/')
    file_hash = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Nouveau champ pour la désactivation
    
    def __str__(self):
        return self.matiere
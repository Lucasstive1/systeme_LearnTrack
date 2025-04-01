from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('professeur', 'professeur'),
        ('Admin', 'Admin'),
        ('Utilisateur', 'Utilisateur'),
    ]
    
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default='Utilisateur')
    phone = models.CharField(max_length=20, unique=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Ajout de related_name pour éviter le conflit
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Ajout de related_name pour éviter le conflit
        blank=True
    )

    def __str__(self):
        return self.username

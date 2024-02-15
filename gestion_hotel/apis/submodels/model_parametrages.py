from django.db import models

class Hotel(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    nombre_chambres = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class Chambre(models.Model):
    numero = models.CharField(max_length=10)
    type_chambre = models.CharField(max_length=100)
    prix_nuit = models.DecimalField(max_digits=8, decimal_places=2)
    est_disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Chambre {self.numero} ({self.type_chambre}) - Prix par nuit: {self.prix_nuit}Fbu"

class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nom

class Equipement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


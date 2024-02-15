from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    date_arrivee = models.DateField()
    date_depart = models.DateField()

    def __str__(self):
        return self.nom
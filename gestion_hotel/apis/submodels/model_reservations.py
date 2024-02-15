from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    chambre = models.ForeignKey('Chambre', on_delete=models.CASCADE)
    date_arrivee = models.DateField(default=timezone.now)
    date_depart = models.DateField(default=timezone.now)
    est_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Réservation de {self.client.nom} pour la chambre {self.chambre.numero}"

    def duree_sejour(self):
        return (self.date_depart - self.date_arrivee).days
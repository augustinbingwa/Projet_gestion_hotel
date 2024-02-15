from django.db import models
from django.utils import timezone

class Facture(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateField(default=timezone.now)
    est_payee = models.BooleanField(default=False)

    def __str__(self):
        return f"Facture pour la réservation {self.reservation.id}"

    def montant_restant(self):
        if self.est_payee:
            return 0
        else:
            return self.montant_total

class Paiement(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField(auto_now_add=True)
    methode = models.CharField(max_length=100)

    def __str__(self):
        return f"Paiement de {self.montant}€ pour la réservation {self.reservation.id}"
from rest_framework import serializers
from gestion_hotel.apis.models import Facture,Paiement

class FactureSerializer(serializers.ModelSerializer):
    montant_restant = serializers.SerializerMethodField()

    class Meta:
        model = Facture
        fields = ['id', 'reservation', 'montant_total', 'date_creation', 'est_payee', 'montant_restant']

    def get_montant_restant(self, obj):
        if obj.est_payee:
            return 0
        else:
            return obj.montant_total

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ['id', 'reservation', 'montant', 'date_paiement', 'methode']

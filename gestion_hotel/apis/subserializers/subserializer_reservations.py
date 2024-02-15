from rest_framework import serializers
from gestion_hotel.apis.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'client', 'chambre', 'date_arrivee', 'date_depart', 'est_active']

    def duree_sejour(self, obj):
        return (obj.date_depart - obj.date_arrivee).days

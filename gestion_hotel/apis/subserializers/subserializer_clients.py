from rest_framework import serializers
from gestion_hotel.apis.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'nom', 'adresse', 'email', 'telephone', 'date_arrivee', 'date_depart']

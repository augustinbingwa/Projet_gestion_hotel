from rest_framework import serializers
from gestion_hotel.apis.models import Hotel,Chambre,Service,Equipement

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'nom', 'adresse', 'telephone', 'description', 'nombre_chambres']

class ChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields = ['id', 'numero', 'type_chambre', 'prix_nuit', 'est_disponible']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'nom', 'description', 'prix']

class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = ['id', 'nom', 'description']

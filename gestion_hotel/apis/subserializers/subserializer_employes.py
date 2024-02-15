from rest_framework import serializers
from gestion_hotel.apis.models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['id', 'nom', 'poste', 'salaire', 'date_embauche']

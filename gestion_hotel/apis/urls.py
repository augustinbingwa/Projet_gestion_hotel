from django.urls import path
from gestion_hotel.apis.views import *

urlpatterns = [
    path('factures/', FactureListView.as_view(), name='facture-list'),
    path('paiements/', PaiementListView.as_view(), name='paiement-list'),*
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('chambres/', ChambreListView.as_view(), name='chambre-list'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('equipements/', EquipementListView.as_view(), name='equipement-list'),
]

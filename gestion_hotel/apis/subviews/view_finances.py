from rest_framework.response import Response
from rest_framework.views import APIView
from gestion_hotel.apis.models import Facture,Paiement
from gestion_hotel.apis.serializers import FactureSerializer,PaiementSerializer

class FactureListView(APIView):
    def get(self, request,pk=None):
        if pk is not None:
            factures = Facture.objects.get(pk=pk)
            serializer = FactureSerializer(factures)
            return Response(serializer.data)
        
        factures = Facture.objects.all()
        serializer = FactureSerializer(factures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        factures = Facture.objects.get(pk=pk)
        serializer = FactureSerializer(factures, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        factures = Facture.objects.get(pk=pk)
        serializer = FactureSerializer(factures, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        factures = Facture.objects.get(pk=pk)
        factures.delete()

class PaiementListView(APIView):
    def get(self, request,pk=None):
        if pk is not None:
            paiements = Paiement.objects.get(pk=pk)
            serializer = PaiementSerializer(paiements)
            return Response(serializer.data)
        
        paiements = Paiement.objects.all()
        serializer = PaiementSerializer(paiements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaiementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        paiements = Paiement.objects.get(pk=pk)
        serializer = PaiementSerializer(paiements, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        paiements = Paiement.objects.get(pk=pk)
        serializer = PaiementSerializer(paiements, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        paiements = Paiement.objects.get(pk=pk)
        paiements.delete()

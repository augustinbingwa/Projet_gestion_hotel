from rest_framework.response import Response
from rest_framework.views import APIView
from gestion_hotel.apis.models import Hotel,Chambre,Service,Equipement
from gestion_hotel.apis.serializers import HotelSerializer,ChambreSerializer,ServiceSerializer,EquipementSerializer

class HotelListView(APIView):
    def get(self, request,pk=None):
        if pk is not None:
            hotels = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(hotels)
            return Response(serializer.data)

        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        hotels = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotels, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        hotels = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotels, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employes = Hotel.objects.get(pk=pk)
        employes.delete()

class ChambreListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            chambres = Chambre.objects.get(pk=pk)
            serializer = ChambreSerializer(chambres)
            return Response(serializer.data)

        chambres = Chambre.objects.all()
        serializer = ChambreSerializer(chambres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChambreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        chambres = Chambre.objects.get(pk=pk)
        serializer = ChambreSerializer(chambres, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        chambres = Chambre.objects.get(pk=pk)
        serializer = ChambreSerializer(chambres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employes = Chambre.objects.get(pk=pk)
        employes.delete()

class ServiceListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            services = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(services)
            return Response(serializer.data)

        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        services = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(services, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        services = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(services, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        services = Service.objects.get(pk=pk)
        services.delete()

class EquipementListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            equipements = Equipement.objects.get(pk=pk)
            serializer = EquipementSerializer(equipements)
            return Response(serializer.data)

        equipements = Equipement.objects.all()
        serializer = EquipementSerializer(equipements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EquipementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        equipements = Equipement.objects.get(pk=pk)
        serializer = EquipementSerializer(equipements, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        equipements = Equipement.objects.get(pk=pk)
        serializer = EquipementSerializer(equipements, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        equipements = Equipement.objects.get(pk=pk)
        equipements.delete()

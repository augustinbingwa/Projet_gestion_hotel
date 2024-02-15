from rest_framework.response import Response
from rest_framework.views import APIView
from gestion_hotel.apis.models import Employe
from gestion_hotel.apis.serializers import EmployeSerializer

class EmployeListView(APIView):
    def get(self, request,pk=None):
        if pk is not None:
            employes = Employe.objects.get(pk=pk)
            serializer = EmployeSerializer(employes)
            return Response(serializer.data)
        
        employes = Employe.objects.all()
        serializer = EmployeSerializer(employes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        employes = Client.objects.get(pk=pk)
        serializer = EmployeSerializer(employes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        employes = Client.objects.get(pk=pk)
        serializer = EmployeSerializer(employes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employes = Client.objects.get(pk=pk)
        employes.delete()

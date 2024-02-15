from rest_framework.response import Response
from rest_framework.views import APIView
from gestion_hotel.apis.models import Client
from gestion_hotel.apis.serializers import ClientSerializer

class ClientListView(APIView):
    def get(self, request,pk=None):
        if pk is not None:
            clients = Client.objects.get(pk=pk)
            serializer = ClientSerializer(clients)
            return Response(serializer.data)

        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        clients = Client.objects.get(pk=pk)
        serializer = ClientSerializer(clients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        clients = Client.objects.get(pk=pk)
        serializer = ClientSerializer(clients, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        clients = Client.objects.get(pk=pk)
        clients.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.response import Response
from rest_framework.views import APIView
from gestion_hotel.apis.models import Reservation
from gestion_hotel.apis.serializers import ReservationSerializer

class ReservationListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            reservations = Reservation.objects.get(pk=pk)
            serializer = ReservationSerializer(reservations)
            return Response(serializer.data)

        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        reservations = Reservation.objects.get(pk=pk)
        serializer = ReservationSerializer(reservations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        reservations = Reservation.objects.get(pk=pk)
        serializer = ReservationSerializer(reservations, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservations = Reservation.objects.get(pk=pk)
        reservations.delete()

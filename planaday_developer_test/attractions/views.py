from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
import json
from .models import (
    Attraction, Inventory, Booking
)
from .serializers import (
    AttractionSerializer, InventorySerializer, BookingSerializer
)
from planaday_developer_test.users.models import User




class AttractionVeiwSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


    # List all Attractions
    def list_Attraction(self, request):
        try:
            Attr_list = Attraction.objects.all()
            serializer = AttractionSerializer(Attr_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            
            return Response(str(e), status=200)

    # Create Attractions
    def create_Attraction(self, request):
        try:
            serializer = AttractionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            
            return Response(str(e), status=200)

    # Detail View of an Attractions
    def get_Attraction(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            print(pk)
            list = Attraction.objects.get(id=pk)
            serializer = AttractionSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
           
            return Response(str(e), status=200)

    
    # Update Attractions
    def update_Attraction(self, request, *args, **kwargs):
        try:
            serializer = AttractionSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = Attraction.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = Attraction.objects.get(id=pk)
                serializer = AttractionSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            
            return Response(str(e), status=200)

    
    # Delete a Attractions
    def delete_Attraction(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = Attraction.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Attraction deleted successfully."}'), status=200)
        except Exception as e:
            
            return Response(str(e), status=200)

class InventoryVeiwSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    
    # List all Inventory
    def list_Inventory(self, request):
        try:
            invent_list = Inventory.objects.all()
            serializer = InventorySerializer(invent_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            
            return Response(str(e), status=200)

    # Create Inventory
    def create_Inventory(self, request):
        try:
            serializer = InventorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            
            return Response(str(e), status=200)


    # Detail view of an Inventory
    def get_Inventory(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            print(pk)
            list = Inventory.objects.get(id=pk)
            serializer = InventorySerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
           
            return Response(str(e), status=200)

    # Update an Inventory
    def update_Inventory(self, request, *args, **kwargs):
        try:
            serializer = InventorySerializer(data=request.data)
            pk = self.kwargs['pk']
            item = Inventory.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = Inventory.objects.get(id=pk)
                serializer = InventorySerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            
            return Response(str(e), status=200)

    
    # Delete an Inventory
    def delete_Inventory(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = Inventory.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Inventory deleted successfully."}'), status=200)
        except Exception as e:
            
            return Response(str(e), status=200)

class BookingVeiwSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # list all Booking
    def list_Booking(self, request):
        try:
            invent_list = Booking.objects.all()
            serializer = BookingSerializer(invent_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            
            return Response(str(e), status=200)

    # Generate Booking and Ticket
    def create_Booking(self, request):
        try:
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                list = Inventory.objects.get(id=serializer.data['attraction'])
                
                # Reducing the Number Ticket available
                list.remain_tickets = int(list.tickets) -  int(serializer.data['noftickets'])
                list.save()

                # Generate Ticket JSON
                Ticket={}   
                list2 = Booking.objects.get(id=serializer.data['id'])
                serializer2 = BookingSerializer(list2)
                list3 = User.objects.get(id=serializer2.data['user'])
                Ticket['Customer'] = list3.username
                Ticket['NumOfTickets'] = serializer2.data['noftickets']
                list4 = Attraction.objects.get(id=serializer2.data['attraction'])
                Ticket['attraction'] = list4.name
                Ticket['description'] = list4.description
                Ticket['datetime'] = serializer.data['date']

                return Response(Ticket, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            
            return Response(str(e), status=200)
 
    # Detail View of a Booking
    def get_Booking(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            print(pk)
            list = Booking.objects.get(id=pk)
            serializer = BookingSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
           
            return Response(str(e), status=200)

    # Update a Booking
    def update_Booking(self, request, *args, **kwargs):
        try:
            serializer = BookingSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = Booking.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = Booking.objects.get(id=pk)
                serializer = BookingSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            
            return Response(str(e), status=200)

    # Delete a booking
    def delete_Booking(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = Booking.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Booking deleted successfully."}'), status=200)
        except Exception as e:
            
            return Response(str(e), status=200)


#Edit Ticket

@api_view(['post'])
# @authentication_classes((TokenAuthentication, ))
# @permission_classes((IsAuthenticated, ))
def update_Booking(request):
    try:
        
        pk = request.POST.get('pk')
        item = Booking.objects.get(id=pk)
        red = request.POST.get('reduce')

        # Reducing the Booked Ticket
        item.noftickets = int(item.noftickets) - int(red)
        item.save() 
        list = Booking.objects.get(id=item.id)
        serializer1 = BookingSerializer(list)
        list1 = Inventory.objects.get(id=serializer1.data['attraction'])

        # Adding the number of Available Tickets
        list1.remain_tickets = int(list1.remain_tickets) + int(red) 
        list1.save()

        # Updated Ticket Generation
        Ticket={}
        list3 = User.objects.get(id=serializer1.data['user'])
        Ticket['Customer'] = list3.username
        Ticket['NumOfTickets'] = serializer1.data['noftickets']
        list4 = Attraction.objects.get(id=serializer1.data['attraction'])
        Ticket['attraction'] = list4.name
        Ticket['description'] = list4.description
        Ticket['datetime'] = serializer1.data['date']
        return Response(Ticket, status=200)
    except Exception as e:
        
        return Response(str(e), status=200)
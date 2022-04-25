
from rest_framework import serializers
from .models import (
    Attraction, Inventory, Booking
)

class AttractionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Attraction;
        fields = ('id','name','description')

    def create(self, validated_data):
        try:
            return Attraction.objects.create(**validated_data);

        except Exception as e:
            print(str(e))

    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.name = validated_data.get('name', instance.name);
            instance.description = validated_data.get('description', instance.description);
            
            instance.save();
            return instance;

        except Exception as e:
            print(str(e))

class InventorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Inventory;
        fields = ('id', 'attraction', 'date', 'tickets', 'remain_tickets', 'rate') 

    def create(self, validated_data):
        try:
            validated_data['remain_tickets'] = validated_data['tickets']
            return Inventory.objects.create(**validated_data);

        except Exception as e:
            print(str(e))

    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.attraction_id = validated_data.get('attraction', instance.attraction);
            # instance.date = validated_data.get('date', instance.date);
            instance.tickets = validated_data.get('tickets', instance.tickets);
            # instance.remain_tickets = validated_data.get('remain_tickets', instance.remain_tickets);
            instance.rate = validated_data.get('rate', instance.rate);
            
            instance.save();
            return instance;

        except Exception as e:
            print(str(e))

class BookingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Booking;
        fields = ('id', 'attraction', 'date', 'noftickets', 'user') 

    def create(self, validated_data):
        try:
            return Booking.objects.create(**validated_data);

        except Exception as e:
            print(str(e))

    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.attraction = validated_data.get('attraction', instance.attraction);
            instance.date = validated_data.get('date', instance.date);
            instance.noftickets = validated_data.get('noftickets', instance.noftickets);
            instance.user = validated_data.get('user', instance.user);
            
            instance.save();
            return instance;

        except Exception as e:
            print(str(e))
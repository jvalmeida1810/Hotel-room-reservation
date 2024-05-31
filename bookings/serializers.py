from rest_framework import serializers
from .models import Hotel, Room, Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        
class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.ReadOnlyField(source='hotel.name') # Campo somente leitura para exibir o nome do hotel.
    class Meta:
        model = Room
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
    def validate(self, data):
        if data['check_out_date'] <= data['check_in_date']: # Verifica se a data de check-out é posterior à de check-in.
            raise serializers.ValidationError(" A data de check-out deve ser posterior à data de check-in.")
        return data
    
    
    

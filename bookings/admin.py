from django.contrib import admin
from .models import Hotel, Room, Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'description')
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','hotel', 'room_number', 'room_type', 'price_per_night', )
    

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room','check_in_date', 'check_out_date', 'created_at')    



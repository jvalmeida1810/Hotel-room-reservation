from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.hotel.name} - Room {self.room_number}'
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room,on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking by {self.user.username} for Room {self.room.room_number} '
    

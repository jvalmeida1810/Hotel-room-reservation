from django.urls import path
from .views import HotelListCreateView, HotelRetrieveUpdateDestroyView, RoomListCreateView, RoomRetrieveUpdateDestroyView, BookingListCreateView, BookingRetrieveUpdateDestroyView

urlpatterns = [
    path('hotel/', HotelListCreateView.as_view(), name= 'hotel'),
    path('hotel/<int:pk>/', HotelRetrieveUpdateDestroyView.as_view(), name='hotel'),
    
    path('room/', RoomListCreateView.as_view(), name='room'),
    path('room/<int:pk>/', RoomRetrieveUpdateDestroyView.as_view(), name='room'),
    
    path('booking/', BookingListCreateView.as_view(), name='booking'),
    path('booking/<int:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking'),
    
]
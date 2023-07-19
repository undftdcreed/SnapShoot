from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('listings/', views.ListingList.as_view(), name="listing_list"),
    path('listings/new/', views.ListingCreate.as_view(), name="listing_create"),
    path('listings/<int:pk>/', views.ListingDetail.as_view(), name="listing_detail"),
    path('listings/<int:pk>/update', views.ListingUpdate.as_view(), name="listing_update"),
    path('listings/<int:pk>/delete', views.ListingDelete.as_view(), name="listing_delete"),
    path('listings/<int:listing_pk>/booking/', views.BookingCreate.as_view(), name='booking_create'),
    path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking_detail'),
    path('bookings/<int:pk>/update/', views.BookingUpdate.as_view(), name='booking_update'),
]
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('listings/', views.ListingList.as_view(), name="listing_list"),
    path('listings/new/', views.ListingCreate.as_view(), name="listing_create"),
]
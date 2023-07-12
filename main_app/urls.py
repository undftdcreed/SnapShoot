from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('listings/', views.ListingList.as_view(), name="listing_list"),
    path('listings/new/', views.ListingCreate.as_view(), name="listing_create"),
    path('listings/<int:pk>/', views.ListingDetail.as_view(), name="listing_detail"),
    path('listings/<int:pk>/update', views.ListingUpdate.as_view(), name="listing_update"),
    path('listings/<int:pk>/delete', views.ListingDelete.as_view(), name="listing_delete"),
    
]
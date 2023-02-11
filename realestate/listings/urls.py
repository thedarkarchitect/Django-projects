from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('listings/<str:pk>', views.listing_retrieve, name='listing_retrieve'),
    
]

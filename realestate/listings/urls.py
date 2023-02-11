from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('listings/<pk>', views.listing_retrieve, name='listing_retrieve'),
    path('add_listing/', views.listing_create, name='add_listing')

]

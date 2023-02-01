from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),

    path('create_order/<str:pk>', views.createOrder, name='createOrder'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete/<str:pk>/', views.delete, name='delete')
]

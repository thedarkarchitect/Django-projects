from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logout/', views.userLogout, name='logout'),

    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('user/', views.userPage, name='user'),

    path('create_order/<str:pk>', views.createOrder, name='createOrder'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete/<str:pk>/', views.delete, name='delete')
]

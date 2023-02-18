from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<str:id>', views.edit, name='edit')
]

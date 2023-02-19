from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/<str:id>', views.info, name='info'),
    path('update/<str:pk>', views.update, name='update')
]

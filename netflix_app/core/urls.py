from django.urls import path
from .views import Home

app_name='core'#namespace

urlpatterns = [
    path('', Home.as_view())
]

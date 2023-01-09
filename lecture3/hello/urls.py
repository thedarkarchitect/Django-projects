from django.urls import path
from . import views

#Whenever a view is added a url pattern to reach that view must be added

urlpatterns = [
    path("", views.index, name="index"),
    path("kev", views.kev, name="kev"),
    path("<str:name>", views.greet, name="greet")
]

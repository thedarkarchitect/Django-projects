from django.urls import path
from .views  import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),#this will be path for the login page
    path('logout/', CustomLoginView.as_view(next_page='login'), name='logout'),#this takes the user to the login view after logout
    path('', TaskList.as_view(), name='tasks'),#this is our home page
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),#this uses the primary key of items to show details or tap into the tasks
    path('task-create/', TaskCreate.as_view(), name='task-create'),#This  view allows to create a task that is sent to the tasks page
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete')
]

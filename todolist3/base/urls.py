from django.urls import path
from .views  import TaskList, TaskDetail, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),#this is our home page
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),#this uses the primary key of items to show details or tap into the tasks
    path('task-create/', TaskCreate.as_view(), name='task-create'),#This  view allows to create a task that is sent to the tasks page
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update')
]

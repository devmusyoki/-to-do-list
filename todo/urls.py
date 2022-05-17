from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateToDo.as_view()),
    path('delete', DeleteToDo.as_view()),
]

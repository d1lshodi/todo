from django.urls import path
from .views import ListCreateTodoView,DetailUpdateDeleteTodoView

urlpatterns = [
    path('',ListCreateTodoView.as_view()),
    path('<pk>',DetailUpdateDeleteTodoView.as_view())
]
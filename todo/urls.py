from django.urls import path
from .views import TodoAPIClass, TodoDetailAPIClass

urlpatterns = [
    path("", TodoAPIClass.as_view()),
    path("<int:todo_id>", TodoDetailAPIClass.as_view()),
]

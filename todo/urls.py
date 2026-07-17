from django.urls import path
from .views import (
    # TodoAPIClass,
    # TodoDetailAPIClass,
    TodoMixinAPIClass,
    TodoMixinDetailAPIClass,
)

urlpatterns = [
    # path("", TodoAPIClass.as_view()),
    # path("<int:todo_id>", TodoDetailAPIClass.as_view()),
    path("", TodoMixinAPIClass.as_view()),
    path("<int:pk>", TodoMixinDetailAPIClass.as_view()),
]

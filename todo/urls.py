from django.urls import path
from .views import (
    # TodoAPIClass,
    # TodoDetailAPIClass,
    # TodoMixinAPIClass,
    # TodoMixinDetailAPIClass,
    # TodoGenericAPIClass,
    # TodoGenericDetailAPIClass,
    TodoViweSetAPIClass,
)
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register("", TodoViweSetAPIClass)

urlpatterns = [
    # path("", TodoAPIClass.as_view()),
    # path("<int:todo_id>", TodoDetailAPIClass.as_view()),
    # path("", TodoMixinAPIClass.as_view()),
    # path("<int:pk>", TodoMixinDetailAPIClass.as_view()),
    # path("", TodoGenericAPIClass.as_view()),
    # path("<int:pk>", TodoGenericDetailAPIClass.as_view()),
    path("", include(router.urls))
]

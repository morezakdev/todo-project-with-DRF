from django.urls import path
from .views import all_todos, todo_details_view

urlpatterns = [path("", all_todos), path("<int:todo_id>", todo_details_view)]

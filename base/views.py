from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.models import todoModel

# Create your views here.


def home_page(request):
    context = {}
    return render(request, "base/index.html", context)


@api_view(["GET"])
def todo_api(request: Request):
    todo = list(todoModel.objects.order_by("privory").all().values("title", "is_done"))
    return Response(todo, status.HTTP_200_OK)

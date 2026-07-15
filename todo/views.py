from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import todoModel
from .serializes import todoserializer

# Create your views here.


@api_view(["GET", "POST"])
def all_todos(request: Request):
    if request.method == "GET":
        todo = list(todoModel.objects.order_by("privory").all())
        todoSerializer = todoserializer(todo, many=True)
        return Response(todoSerializer.data, status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def todo_details_view(request: Request, todo_id: int):
    try:
        todo = todoModel.objects.get(pk=todo_id)
    except todoModel.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = todoserializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = todoserializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        todo.delete()
        return Response(None, status.HTTP_200_OK)

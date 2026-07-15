from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import todoModel
from .serializes import todoserializer

# Create your views here.


@api_view(["GET","POST"])
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

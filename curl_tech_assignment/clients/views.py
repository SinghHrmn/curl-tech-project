from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Client
from .serializers import ClientSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all().filter(login_state='a')
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def allow_client(request, id):
    if request.method == 'PUT':
        model = get_object_or_404(Client, pk=id)
        data = {"login_state": "y"}
        serializer = ClientSerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def deny_client(request, id):
    if request.method == 'PUT':
        model = get_object_or_404(Client, pk=id)
        data = {"login_state": "n"}
        serializer = ClientSerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client_status(request, id):
    if request.method == 'GET':
        clients = Client.objects.all().filter(pk=id)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

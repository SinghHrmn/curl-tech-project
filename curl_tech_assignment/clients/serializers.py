from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Client

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ( 'pk', 'username', 'company_name', 'login_state')


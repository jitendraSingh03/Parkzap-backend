from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.serializer import contact_Info_Serializer
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import contact_info

class contactList(ListAPIView):
    queryset=contact_info.objects.all()
    serializer_class=contact_Info_Serializer

class contactCreate(CreateAPIView):
    queryset=contact_info.objects.all()
    serializer_class=contact_Info_Serializer
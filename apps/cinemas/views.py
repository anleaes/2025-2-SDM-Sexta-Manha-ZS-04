from django.shortcuts import render
from rest_framework import viewsets
from .models import Cinema
from .serializer import CinemaSerializer

# Create your views here.
class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer  
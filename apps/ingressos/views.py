from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ingresso
from .serializer import IngressoSerializer

# Create your views here.
class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo'] 
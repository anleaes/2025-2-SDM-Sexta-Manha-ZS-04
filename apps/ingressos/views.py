from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingresso
from .serializer import IngressoSerializer

# Create your views here.
class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer  
from django.shortcuts import render
from rest_framework import viewsets
from .models import Filme
from .serializer import FilmeSerializer

# Create your views here.
class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer  
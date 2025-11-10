from django.shortcuts import render
from rest_framework import viewsets
from .models import Sessao
from .serializer import SessaoSerializer

class SessaoViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer
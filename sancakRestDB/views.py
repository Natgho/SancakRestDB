from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import GirisSerializer
from .models import Giris
from rest_framework import permissions


class GirisViewSet(viewsets.ModelViewSet):
    queryset = Giris.objects.all().order_by('ehliyetno')
    serializer_class = GirisSerializer
    permission_classes = [permissions.IsAuthenticated]

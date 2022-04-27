# Django
from django_filters.rest_framework import DjangoFilterBackend
# Rest-Framework
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
# Project
from .serializers import CoverCategorySerializer, CarsCategorySerializer, CoverSerializer
from .models import CoverCategory, CarsCategory, Cover


class CoverViewSet(ModelViewSet):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['car_name', 'cover', 'color']
    search_fields = ['car_name', 'cover', 'color']
    ordering_fields = ['price', ]

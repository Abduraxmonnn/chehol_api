# Django
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
# Rest-Framework
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Project
from .serializer import NewsSerializer

from .models import News


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all().order_by('id')

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super(NewsViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super(NewsViewSet, self).get_queryset()
        return queryset


class NewsDetailAPIView(RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = NewsSerializer
        return super(NewsDetailAPIView, self).retrieve(request, *args, **kwargs)

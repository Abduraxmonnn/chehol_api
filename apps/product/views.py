# Django
from django_filters.rest_framework import DjangoFilterBackend
# Rest-Framework
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
# Project
from .serializers import CoverCategorySerializer, CarsCategorySerializer, CoverSerializer
from .models import CoverCategory, CarsCategory, Cover


class CoverCategoryCreateAPIView(CreateAPIView):
    serializer_class = CoverCategorySerializer
    queryset = CoverCategory.objects.all()

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        cover_category_data = request.data

        new_patient = CoverCategory.objects.create(material=cover_category_data['material'])
        new_patient.save()
        serializer = CoverCategorySerializer(new_patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CoverCategoryListAPIView(ListAPIView):
    serializer_class = CoverCategorySerializer
    queryset = CoverCategory.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'material']
    ordering_fields = ['id']


class CoverCategoryRetrieveAPIVIew(RetrieveAPIView):
    serializer_class = CoverCategorySerializer
    queryset = CoverCategory.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'material']
    ordering_fields = ['id']


class CoverCategoryUpdateViewSet(ModelViewSet):
    serializer_class = CoverCategorySerializer
    queryset = CoverCategory.objects.filter().order_by('id')
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'material']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = super(CoverCategoryUpdateViewSet, self).get_queryset()
        return queryset


class CoverCategoryDestroyAPIView(DestroyAPIView):
    serializer_class = CoverCategorySerializer
    queryset = CoverCategory.objects.all()


class CarsCategoryCreateUpdateDestroyViewSet(ModelViewSet):
    serializer_class = CarsCategorySerializer
    queryset = CarsCategory.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        return queryset

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class CarsCategoryListAPIView(ListAPIView):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['car_name', 'car_model']
    search_fields = ['car_name', 'car_model']


class CarsRetrieveAPIView(RetrieveAPIView):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CoverSerializer
        return super(CarsRetrieveAPIView, self).retrieve(request, *args, **kwargs)


class CoverCreateUpdateViewSet(ModelViewSet):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        return queryset


class CoverListViewSet(ModelViewSet):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['car_name', 'cover', 'color']
    search_fields = ['car_name', 'cover', 'color']
    ordering_fields = ['car_name', 'color', 'price']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        cover = self.paginate_queryset(queryset)
        if cover is not None:
            serializer = self.get_serializer(cover, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CoverRetrieveAPIView(RetrieveAPIView):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['car_name', 'cover', 'color']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CoverSerializer
        return super(CoverRetrieveAPIView, self).retrieve(request, *args, **kwargs)


class CoverDestroyViewSet(ModelViewSet):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()

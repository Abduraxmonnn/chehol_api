# Rest-Framework
from rest_framework import serializers

# Project
from .models import CoverCategory, CarsCategory, Cover


class CoverCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CoverCategory
        fields = ('material', )


class CarsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CarsCategory
        fields = ['car_name', 'car_model']


class CoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cover
        fields = '__all__'

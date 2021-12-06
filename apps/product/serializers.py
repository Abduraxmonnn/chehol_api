# Rest-Framework
from rest_framework import serializers, status
# Project
from rest_framework.response import Response

from .models import CoverCategory, CarsCategory, Cover


class CoverCategorySerializer(serializers.ModelSerializer):

    def post(self, validated_data):
        new_category = super().create(validated_data=validated_data)
        new_category.save()
        return new_category

    def get(self, request):
        category = request.category
        serializer = CoverCategorySerializer(instance=category, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    class Meta:
        model = CoverCategory
        fields = '__all__'


class CarsCategorySerializer(serializers.ModelSerializer):

    def post(self, validated_data):
        new_car_category = CarsCategory.objects.create(**validated_data)
        new_car_category.save(foo=validated_data['car_name', 'car_model'])
        return new_car_category

    def get(self, request):
        car = request.car
        serializer = CarsCategorySerializer(instance=car, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, instance, validated_data):
        instance.car_name = validated_data.get('car_name', None)
        instance.car_model = validated_data.get('car_model', None)
        instance.save()
        return instance

    class Meta:
        model = CarsCategory
        fields = ('car_name', 'car_model')


class CoverSerializer(serializers.ModelSerializer):

    def post(self, request, validated_data):
        new_product = Cover.objects.create(**validated_data)
        new_product.save(foo=validated_data['car_name', 'cover', 'pattern', 'color',
                                            'price', 'image', 'phone_number', 'instagram', 'telegram'])
        return new_product

    def get(self, request):
        product = request.product
        serializer = CoverSerializer(instance=product, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    class Meta:
        model = Cover
        fields = '__all__'

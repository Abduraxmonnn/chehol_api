from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'theme', 'description', 'category_news', 'image', 'created_date')

    def create(self, validated_data):
        theme = validated_data.get('theme', None)
        category_news = validated_data.get('end_date', None)
        if theme is None and category_news:
            raise serializers.ValidationError({"error": "You cannot give theme and category news please set"})
        quiz = self.Meta.model.objects.create(**validated_data)
        return quiz

    def update(self, instance, validated_data):
        instance.theme = validated_data.get('theme', None)
        instance.description = validated_data.get('description', None)
        instance.category_news = validated_data.get('category_news', None)
        instance.save()
        return instance

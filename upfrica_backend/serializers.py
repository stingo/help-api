from rest_framework import serializers
from .models import HelpCategory, HelpArticle

class HelpCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpCategory
        fields = ['id', 'name', 'slug']

class HelpArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpArticle
        fields = [
            'id', 'title', 'slug', 'date', 'lastmod',
            'tags', 'is_published', 'summary', 'body',
            'images', 'tips', 'note'
        ]

    def validate(self, data):
        print("🔍 Validating HelpArticle data:", data)
        return super().validate(data)
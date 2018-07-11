from rest_framework import serializers

from .models import Category, Writing


class CategorySerializer(serializers.ModelSerializer):
    """文章分类序列化器"""

    class Meta:
        model = Category
        fields = ("name",)


class WritingSerializer(serializers.ModelSerializer):
    """文章序列化器"""

    class Meta:
        model = Writing
        fields = "__all__"


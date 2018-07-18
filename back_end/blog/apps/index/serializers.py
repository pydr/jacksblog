import re

from rest_framework import serializers

from .models import Category, Writing, SubscribeEmail, MainPic


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
        depth = 1


class SubscribeEmailSerializer(serializers.ModelSerializer):
    """订阅序列化器"""
    email = serializers.EmailField(label="订阅邮箱", required=True, allow_null=False, allow_blank=False)

    def validate_email(self, attr):
        """
        校验email
        :param attr: body数据
        :return:
        """
        if not attr:
            raise serializers.ValidationError("Email不能为空！")
        if not re.match(r"^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", attr):
            raise serializers.ValidationError("邮箱格式错误")

        count = SubscribeEmail.objects.filter(email=attr).count()

        if count > 0:
            raise serializers.ValidationError("您已订阅过本站，无需重复订阅！")

        return attr

    def create(self, validated_data):
        """写入数据库"""

        email = super().create(validated_data)
        email.save()

        return email

    class Meta:
        model = SubscribeEmail
        fields = "__all__"


class MainPicSerializer(serializers.ModelSerializer):
    """轮播图序列化器"""

    class Meta:
        model = MainPic
        fields = "__all__"
        depth = 1




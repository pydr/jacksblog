from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from index.serializers import CategorySerializer, WritingSerializer
from .models import Category, Writing


class CategoryList(APIView):
    """文章分类列表视图"""
    def get(self, request):
        """
        获取文章列表
        :param request:
        :return:
        """

        # 查询所有文章分类
        query_set = Category.objects.all()

        serializer = CategorySerializer(query_set, many=True)

        return Response(serializer.data)


class WritingList(APIView):

    def get(self, request):
        queryset = Writing.objects.all()

        serializer = WritingSerializer(queryset, many=True)

        return Response(serializer.data)




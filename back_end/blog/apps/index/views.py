from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from index.serializers import CategorySerializer, WritingSerializer
from .models import Category, Writing


class CategoryListView(APIView):
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


class WritingListView(APIView):
    """文章列表页"""
    def get(self, request):
        queryset = Writing.objects.all().order_by("read_count")[:5]

        serializer = WritingSerializer(queryset, many=True)

        return Response(serializer.data)


class RencentPostView(APIView):
    """最近更新列表页"""
    def get(self, request):
        queryset = Writing.objects.all().order_by("update_time")[:3]

        serializer = WritingSerializer(queryset, many=True)

        return Response(serializer.data)


class WritingDetailView(RetrieveAPIView):
    """文章详情视图"""

    queryset = Writing.objects.all()
    serializer_class = WritingSerializer
    def get(self, request, pk):

        return self.retrieve(request, pk)


class TechnologyListView(APIView):
    """Tenchnology模块列表页视图"""
    def get(self, request):
        queryset = Writing.objects.filter(category_id__exact=1).order_by("-update_time")[:4]

        serializer = WritingSerializer(queryset, many=True)

        return Response(serializer.data)


class LifeListView(APIView):
    """Life 模块列表页视图"""
    def get(self, request):
        queryset = Writing.objects.filter(category_id__exact=2).order_by("-update_time")[:4]

        serializer = WritingSerializer(queryset, many=True)

        return Response(serializer.data)




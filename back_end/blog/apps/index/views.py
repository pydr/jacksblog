from django.shortcuts import render

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from index.serializers import CategorySerializer, WritingSerializer, SubscribeEmailSerializer, MainPicSerializer
from .models import Category, Writing, MainPic, Comment


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
    pagination_class = None
    def get(self, request):
        queryset = Writing.objects.all().order_by("read_count")[:5]

        serializer = WritingSerializer(queryset, many=True)

        return Response(serializer.data)


class RencentPostView(APIView):
    """最近更新列表页"""
    def get(self, request):
        queryset = Writing.objects.all().order_by("update_time")[:4]

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


class SubscribeView(CreateAPIView):
    """文章订阅模块"""
    serializer_class = SubscribeEmailSerializer


class MainPicView(APIView):
    """首页轮播图视图"""
    def get(self, request):
        queryset = MainPic.objects.filter(is_delete__exact=0).order_by("-update_time")

        serializer = MainPicSerializer(queryset, many=True)

        return Response(serializer.data)


class PopularPostView(APIView):
    """最受欢迎列表页"""
    def get(self, request):
        queryset = Writing.objects.all().order_by("-read_count")[:4]

        serializer = WritingSerializer(queryset, many=True)

        return Response(serializer.data)


class BlogListView(ListAPIView):
    """blog 列表页视图"""
    serializer_class = WritingSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('update_time', )

    def get_queryset(self):
        return Writing.objects.all()













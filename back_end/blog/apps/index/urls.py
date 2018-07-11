from django.urls import path

from . import views

urlpatterns = [

    path('categories/', views.CategoryList.as_view()),  # 获取分类
    path('writings/', views.WritingList.as_view())
]

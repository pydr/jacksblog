from django.urls import path

from . import views

urlpatterns = [

    path('categories/', views.CategoryListView.as_view()),  # 获取分类
    path('posts/', views.WritingListView.as_view()),
    path('recent_posts/', views.RencentPostView.as_view()),
    path('post/<int:pk>/', views.WritingDetailView.as_view()),
]

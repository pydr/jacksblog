from django.urls import path

from . import views

urlpatterns = [

    path('categories/', views.CategoryListView.as_view()),  # 获取分类
    path('posts/', views.WritingListView.as_view()),
    path('recent_posts/', views.RencentPostView.as_view()),
    path('post/<int:pk>/', views.WritingDetailView.as_view()),
    path('technologies/', views.TechnologyListView.as_view()),
    path('life/', views.LifeListView.as_view()),
    path('subscribe/', views.SubscribeView.as_view()),
    path('main_pic/', views.MainPicView.as_view()),
    path('popular_post/', views.PopularPostView.as_view()),
    path('blog/post', views.BlogListView.as_view()),
]

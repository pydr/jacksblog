from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from blog.utils.models import BaseModel


class Category(BaseModel):
    """文章分类模型类"""
    name = models.CharField(max_length=10, verbose_name="分类名称")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        db_table = "tb_categories"
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name


class Writing(BaseModel):
    """文章模型类"""

    title = models.CharField(max_length=64, default="无标题", verbose_name="文章标题")
    author = models.CharField(max_length=20, default="admin", verbose_name="作者")
    summary = models.CharField(max_length=500, default="无摘要", verbose_name="摘要")
    content = RichTextUploadingField(default="", verbose_name="文章正文")
    read_count = models.IntegerField(default=0, verbose_name="阅读量")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="文章分类")

    class Meta:
        db_table = "tb_writings"
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class Comment(BaseModel):
    """评论模型类"""

    comment_author = models.CharField(max_length=20, verbose_name="评论作者")
    comment_avatar = models.CharField(max_length=64, default="default.jpg", verbose_name="评论头像")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE, verbose_name="所属文章")

    class Meta:
        db_table = "comments"
        verbose_name = "评论"
        verbose_name_plural = verbose_name

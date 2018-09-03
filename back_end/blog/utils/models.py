"""
模型类基类
共有字段
"""
from django.db import models


class BaseModel(models.Model):
    """模型类基类 共有字段"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True  # 声明该模型类是抽象类，不迁移为数据表

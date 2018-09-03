from django.db import models

# Create your models here.
from blog.utils.models import BaseModel


class Album(BaseModel):
    """相册类"""
    title = models.CharField(max_length=32, default="请填写标题", verbose_name="照片标题")
    pic = models.ImageField(verbose_name="照片")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        db_table = "tb_album"
        verbose_name = "相册"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

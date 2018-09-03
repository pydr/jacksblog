from django.contrib import admin

# Register your models here.
from . import models


class PostAdmin(admin.ModelAdmin):
    """保存文章时生成详情页静态页面"""
    def save_model(self, request, obj, form, change):
        obj.save()
        from celery_tasks.html.tasks import generate_detail_page
        generate_detail_page(obj.id)


admin.site.register(models.Category)
admin.site.register(models.Writing, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.MainPic)

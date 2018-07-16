from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Category)
admin.site.register(models.Writing)
admin.site.register(models.Comment)
admin.site.register(models.MainPic)

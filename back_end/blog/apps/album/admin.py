from django.contrib import admin

# Register your models here.
from album import models

admin.site.register(models.Album)

# Generated by Django 2.0.7 on 2018-07-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180715_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='writing',
            name='feature_pic',
            field=models.ImageField(default='', upload_to='', verbose_name='文章特征图'),
        ),
    ]

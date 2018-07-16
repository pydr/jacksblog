# Generated by Django 2.0.7 on 2018-07-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_writing_feature_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('email', models.CharField(max_length=64, verbose_name='订阅邮箱')),
                ('is_delete', models.BooleanField(default=False, verbose_name='退订')),
            ],
            options={
                'verbose_name': '订阅邮箱',
                'verbose_name_plural': '订阅邮箱',
                'db_table': 'subscribe',
            },
        ),
    ]

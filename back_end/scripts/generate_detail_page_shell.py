#!/usr/bin/env python
import datetime
import sys

from django.conf import settings
from django.template import loader

sys.path.insert(0, '../')
sys.path.insert(0, '../blog/apps')

import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings.settings_dev'

import django
django.setup()

from index.models import Writing


def generate_detail_page(post_id):
    """生成静态文章详情页面"""
    post = Writing.objects.get(id=post_id)
    latest_posts = Writing.objects.all().order_by("-update_time")[:4]
    print("正在渲染页面>> {}.html".format(post_id))

    context = {
        "title": post.title,
        "summary": post.summary,
        "category": post.category.name,
        "update_time": post.update_time,
        "content": post.content,
        "feature_pic": post.feature_pic,
        "latest_posts": latest_posts,
    }

    # 渲染模板并生成html页面
    template = loader.get_template('single.html')
    html_text = template.render(context).encode()
    file_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, 'post/%d.html' % post_id)
    with open(file_path, "wb") as f:
        f.write(html_text)


if __name__ == '__main__':
    posts = Writing.objects.all()
    for post in posts:
        generate_detail_page(post.id)
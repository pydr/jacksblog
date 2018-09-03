from celery_tasks.main import app
import os

from django.conf import settings
from django.template import loader

from index.models import Writing


@app.task(name='generate_detail_page')
def generate_detail_page(post_id):
    """生成静态文章详情页面"""
    post = Writing.objects.get(id=post_id)
    print("开始渲染")
    print(type(post.feature_pic))
    print(post.feature_pic)

    context = {
        "title": post.title,
        "summary": post.summary,
        "category": post.category.name,
        "update_time": post.update_time,
        "content": post.content,
        "feature_pic": post.feature_pic
    }

    # 渲染模板并生成html页面
    template = loader.get_template('single.html')
    html_text = template.render(context).encode()
    file_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, 'post/%d.html' % post_id)
    with open(file_path, "wb") as f:
        f.write(html_text)


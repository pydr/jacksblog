import os

from django.conf import settings
from django.template import loader

from index.models import Writing


def generate_detail_page(post_id):
    """生成静态文章详情页面"""
    post = Writing.objects.get(id=post_id)

    context = {
        "title": post.title,
        "category": post.category.name,
        "update_time": post.update_time,
        "author": post.author,
        "comment_count": post.read_count,
        "content": post.content
    }

    # 渲染模板并生成html页面
    template = loader.get_template('single.html')
    html_text = template.render(context).encode()
    file_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, '%d.html' % post_id)
    with open(file_path, "wb") as f:
        f.write(html_text)





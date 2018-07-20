import os

from django.conf import settings
from django.template import loader

from index.models import MainPic, Writing


def generate_index_page():
    """生成静态首页页面"""
    top_pics = MainPic.objects.filter(is_delete__exact=False)
    latest_posts = Writing.objects.all().order_by("-update_time")[:4]



    context = {
        "top_pics": top_pics,
        "latest_posts": latest_posts,
    }

    # 渲染模板并生成html页面
    template = loader.get_template('index.html')
    html_text = template.render(context).encode()
    file_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, 'index.html')
    with open(file_path, "wb") as f:
        f.write(html_text)
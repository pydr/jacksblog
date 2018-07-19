from celery import Celery

# 为celery使用django配置文件进行设置
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings.settings_dev'

# 1. 创建Celery应用对象
app = Celery("blog")

# 2. 加载Celery配置
app.config_from_object("celery_tasks.config")

# 注册异步任务到Celery中
app.autodiscover_tasks(["celery_tasks.html"])  # 自动会查找到任务包里面tasks模块

# 最终在终端里面运行Celery
# celery -A 主程序的包路径 worker -l info
# 一般从后端的项目根目录下，执行上面的命令：
# celery -A celery_tasks.main worker -l info
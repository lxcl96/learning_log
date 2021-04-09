from django.contrib import admin
# .点 让Django在admin.py所在目录查找models.py文件
from .models import Topic,Entry

# Register your models here.
# 新建了模型后，迁移数据库，在此处注册新模型

admin.site.register(Topic)
admin.site.register(Entry)
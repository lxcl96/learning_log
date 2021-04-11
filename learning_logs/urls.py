# @Time : 2021-04-11 15:56
# @Author : ly
# @File : urls.py.py
# @Software : PyCharm
"""定义learning_logs 的URL模式"""
from django.urls import path
# 导入当前目录下的views模块
from . import views


# 声明各个应用app名称，以便于区分开来
app_name = 'learning_logs'
urlpatterns = [
    # 主页
    # 第一个参数为 地址栏的正则表达式
    # 第二个参数为 此应用app下的index() 函数
    # 第三个参数为 将这个URL模式的名称指定为index 这样能够在代码的其他地方引用它 而不是写URL
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 配置具体Entry 内容
    # 第二部分 /<int:topic_id>/ 与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名为topic_id的参数中
    # 主要目的是为了 将具体某条信息的 id即topic_id 传递给 view中的 topic函数
    path('topics/<int:topic_id>/', views.topic, name='topic'),

]
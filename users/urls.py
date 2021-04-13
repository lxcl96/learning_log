# @Time : 2021-04-13 20:51
# @Author : ly
# @File : urls.py.py
# @Software : PyCharm
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证URL 使用django自带的登录
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]
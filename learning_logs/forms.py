# @Time : 2021-04-11 21:07
# @Author : ly
# @File : forms.py.py
# @Software : PyCharm
from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    # 最简单的模板只包含Meta类，他告诉Django根据哪个模型创建表单以及在表单中包含哪些字段
    class Meta:
        model = Topic
        # 根据 模型Topic 创建表单其中只包含字段text
        fields = ['text']
        # 让django 不要为text生成标签
        labels = {'text': ''}
        
# @Time : 2021-04-11 21:07
# @Author : ly
# @File : forms.py.py
# @Software : PyCharm
from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    # 最简单的模板只包含Meta类，他告诉Django根据哪个模型创建表单以及在表单中包含哪些字段
    class Meta:
        model = Topic
        # 根据 模型Topic 创建表单其中只包含字段text
        fields = ['text']
        # 让django 不要为text生成标签
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 定义一个小部件widgets，这是一个html表单元素，如单行文本框，多行文本区域或下拉列表
        # 通过自定义小组件来覆盖django默认的小组件，将文本区域的宽度设置为80列而不是默认的40列
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

# 代表Django从服务器收到request请求
def topics(request):
    """显示所有主题"""
    topics  = Topic.objects.order_by('date_added')
    # 定义一个可以发送给模板的上下文，为字典类型
    # 其中的 键-key为用来访问数据库的名称，值-value为数数据库中存放的实际数据
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# 获取请求的参数 request请求 和传递的topic_id 参数
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    # 下面为查询操作，可以在shell中使用便于快速排查出错误
    topic = Topic.objects.get(id=topic_id)
    # 增加时间倒叙排序
    entries = topic.entry_set.order_by('-date_added')
    # 上下文字典 传递topic 和外键关联 entries
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
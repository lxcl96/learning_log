from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


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


# 处理两种情况:1、刚进入new_topic页面显示空表单2、对提交的表单数据进行处理， 并将用户重定向到页面topics
def new_topic(request):
    """ 添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据：对数据进行处理
        form = TopicForm(data=request.POST)
        # 如果表单数据有效
        if form.is_valid():
            form.save()
            # 正确提交后重定向到topics.html
            return redirect('learning_logs:topics')

    # 显示空表单或者表单数据无效
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """在特定的主题添加新条目"""
    # 获取要增加条目的 主题
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        # 表单数据来自于 页面提交
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # 有外键约束的不仅仅要存储 表单数据 而且还要存储 外键topic 以便将其关联起来
            # commit=False 让django创建一个新的条目但是不存储到数据库
            new_entry = form.save(commit=False)
            # 将要增加的条目关联到主题上
            new_entry.topic = topic
            new_entry.save()
            # 将其重定向到 格式为【appname：urlname】 因为这个视图函数需要两个参数，所以再传递一个topic值
            return redirect('learning_logs:topic', topic_id=topic_id)
    # 传递 主题和 条目
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
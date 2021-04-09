from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    # char型
    text = models.CharField(max_length=200)
    # DateTimeField记录日期和时间的数据
    date_added = models.DateTimeField(auto_now_add=True)

    # 调用__str__()来显示模型的简单表示，这里用其返回存储在属性text中的字符串
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # topic是类（表）Topic 的外键实例，CASCADE 级联删除 在删除主题Topic时 对应的topic也会被删除
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 大文本型
    text = models.TextField()
    # 创建时间
    date_added = models.DateTimeField(auto_now_add=True)

    # Meta类 存储 用于管理 模型 的额外信息
    class Meta:
        # 这里它让我们能够设置一个特殊属性，让Django在需要时使用Entris来表示多个条目
        # 如果没有这个类，Django将使用Entry来表示多个条目
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        # 只显示前50个字符，点击显示全部
        return f"{self.text[:50]}..."




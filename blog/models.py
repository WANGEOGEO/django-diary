from django.db import models


# Create your models here.

class Article(models.Model):
    # 规定好题目长度限制和默认值
    title = models.CharField(max_length=32, default='Title')
    # 内容允许为空
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

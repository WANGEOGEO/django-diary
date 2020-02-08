from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    # 处理请求的前提是接受请求s
    # 获得全部的article列表,all返回的是django自带的一个东西。
    articles = models.Article.objects.all()
    print(articles)
    # 第二个是对应的html界面，第一个就是request。
    # 第三个参数是键值对dict，给前端传递数据的。键为参数名。
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/article_page.html", {"article": article})

def edit_page(request, article_id):
    if str(article_id) == "0":
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    print(article_id)
    print(type(article))
    return render(request, "blog/edit_page.html", {"article": article})


def edit_action(request):
    # 先获取POST请求的内容，括号中第二个参数为默认值
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    # 然后创建新的Article对象
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk = article_id)
        article.content = content
        article.title = title
        article.save()
        return render(request, "blog/article_page.html", {"article": article})
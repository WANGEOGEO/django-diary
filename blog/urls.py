from django.conf.urls import url
from . import views


# 必须得明确app名字
app_name = 'blog'

urlpatterns = [
    # 所以啊，这里就不需要再管127.0.0.1:8000/blog/这一部分了，直接写后面那一部分就可以了。
    url(r'^index/$', views.index),
    # 后面的数字的“参数名”一定要留下和view里面写的一样的变量名，比如这里的article_id.
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action')
]
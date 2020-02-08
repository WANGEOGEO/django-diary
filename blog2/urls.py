from django.conf.urls import url
from . import views

urlpatterns = [
    # 所以啊，这里就不需要再管127.0.0.1:8000/index/这一部分了，直接写后面那一部分就可以了。
    url(r'^index/$', views.index)
]
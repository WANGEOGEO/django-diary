from django.shortcuts import render

# Create your views here.
def index(request):
    # 处理请求的前提是接受请求
    # 第二个是对应的html界面，第一个就是request。
    # 第三个参数是键值对dict，给前端传递数据的。键为参数名。
    return render(request, 'blog2/index.html')